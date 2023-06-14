# transcribe-yt.py
# script to use whisper to transcribe youtube videos
import re
import pandas as pd
import whisper
import yt_dlp as youtube_dl
import json
import os
import warnings
import pprint
from termcolor import colored
#warnings.filterwarnings("ignore", category=DeprecationWarning, module='whisper.*')
warnings.filterwarnings("ignore", module='whisper.*')

class getMetadata:
    def __init__(self):
    #def __init__(self, errors=None, output=None):    
        self.channel_metadata = {}
    #    self.errors = errors if errors is not None else {}
    #    self.output = output if output is not None else {}

    # get channel list
    def get_channel_list(self, channel_url, channel_name, errors=None, output=None):
    #def get_channel_list(self, channel_url, channel_name):
        errors = errors if errors is not None else {}
        output = output if output is not None else {}
        options = {
            'extract_flat': True,
        }
        try:
            with youtube_dl.YoutubeDL(options) as downloader:
                print(f"[get_channel_list] Getting channel list for {channel_name}...")
                info_dict = downloader.extract_info(channel_url, download=False)
                # save the urls in a txt file
                filename = f'data/channel_list_urls-[{channel_name}].txt' 
                print(f"[get_channel_list] Saving channel list urls to {filename}")
                # SKIP unless debugging
                json_string = json.dumps(info_dict, indent=4)
                print(f"DEBUG: json_string: {json_string}")
                output[channel_url] = filename
                print(f"[get_channel_list] DEBUG: output: {output}")
                with open(filename, 'w') as f:
                    for entry in info_dict['entries']:
                        video_url = entry['url']
                        self.channel_metadata[video_url] = self.get_video_metadata(video_url)
                        f.write(video_url + '\n')
                print(f"[get_channel_list] Done getting channel list and saving to file {filename}")
                #print(f"[get_channel_list] DEBUG self.channel_metadata: {self.channel_metadata}")
                # add url to output dictionary

            return info_dict
        except KeyError as e:
            print(f"[get_channel_list] Error occurred during channel list generation for {channel_name}")
            msg = "Error related to missing key [entries] likely due to incorrect url for channel"
            print(f"[get_channel_list] Error message: {str(e)}")
            print(f"[get_channel_list] Error commentary: {msg}")
            print(f"[get_channel_list] Error type: {type(e)}")
            errors[channel_url] = str(e) + "\n" + msg # store error message & commentary in the dictionary
        except youtube_dl.utils.DownloadError as e:
            print(f"[get_channel_list] Download Error occurred during channel list generation for {channel_name}")
            print(f"[get_channel_list] Download Error message: {str(e)}")
            print(f"[get_channel_list] Error type: {type(e)}")
            errors[channel_url] = str(e) # Store the error message in the dictionary
            return None
        except Exception as e:
            print(f"[get_channel_list] Error occurred during channel list generation for {channel_name}")
            print(f"[get_channel_list] Error message: {str(e)}")
            print(f"[get_channel_list] Error type: {type(e)}")
            errors[channel_url] = str(e) # Store the error message in the dictionary
            return None

    # get video metadata
    def get_video_metadata(self, url):
        print(f"[get_video_metadata] Starting process...{url}")
        options = {}
        try:
            with youtube_dl.YoutubeDL(options) as downloader:
                info_dict = downloader.extract_info(url, download=False)
                metadata = {
                    'url': url,
                    'title': info_dict.get('title'),
                    'description': info_dict.get('description'),
                    'uploader': info_dict.get('uploader'),
                    'upload_date': info_dict.get('upload_date'),
                    'duration': info_dict.get('duration'),
                    'view_count': info_dict.get('view_count'),
                    'like_count': info_dict.get('like_count'),
                    'id': info_dict.get('id'),
                    'categories': info_dict.get('categories'),
                    'tags': info_dict.get('tags'),
                    
                    # Add more fields as needed
                }
        except Exception as e:
            print(f"[get_video_metadata] Error occurred during metadata retrieval for {url}")
            print(f"[get_video_metadata] Error message: {str(e)}")
            print(f"[get_video_metadata] Error type: {type(e)}")
            self.errors[url] = str(e) # Store the error message in the dictionary
            return None
        print("[get_video_metadata] Done getting video metadata")
        return metadata
    
class downloadSource:
    # download audio from youtube 
    def download_audio(self, url):
        print(f"[download_audio] Initiating download with youtube...{url}")
        options = {
        'outtmpl': 'data/input/%(title)s.%(ext)s',  # Download into 'data/input' directory
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'prefer_ffmpeg': True,
        }
        with youtube_dl.YoutubeDL(options) as downloader:
            downloader.download([url])
            download_file = downloader.prepare_filename(downloader.extract_info(url, download=False)).replace(".webm", ".mp3")
        if (download_file is None):
            print("[download_audio] Download failed")
            return None
        else:
            print("[download_audio] Done downloading")
            return download_file

    # call download source file as mp3 and save to data/input   
    def save_to_mp3(self, url):
        print(f"[save-to-mp3] calling download_audio...{url}")
        filename = self.download_audio(url)
        if (filename is None):
            print("[save-to-mp3] Download failed")
            return None
        else:
            filename = filename.replace('.m4a', '.mp3')
            print(f"[save-to-mp3] Complete Filename: {filename}")
            return filename

class myTextSplitter:
    def __init__(self, text, n):
        self.text = text
        self.n = n

    def split_into_sentences(self):
        print("[split_into_sentences] splitting transcription into sentences")
        if self.text == "":
            raise ValueError("[split_into_sentences] Input text cannot be empty.")
        #print(f"DEBUG: self.text: {self.text}")
        #print(f"DEBUG: First 20 characters of text: {self.text['text'][:20]}")
        sentences = re.split("(?<=[.!?]) +", self.text['text'])
        print(f"[split_into_sentences] Done splitting into sentences (n={len(sentences)})")
        return sentences

    def save_as_txt(self, filename, metadata, model):
        print(f"[save_as_txt] Formatting metadata and transcription text")
        try:
            with open(filename, 'w') as f:
                if metadata is not None:
                    for key, value in metadata.items():
                        f.write(f'{key}: {value}\n')
                    f.write('\n')
                sentences = self.split_into_sentences()
                if sentences is None:
                    return None
                else:
                    print(f"[save_as_txt] Saving sentences to txt file {filename}")
                    f.write(f'transcription model: {model}\n')
                    f.write(f'transcription text:\n')
                    for sentence in sentences:
                        f.write(sentence + '\n')
            print(f"[save_as_txt] Done saving metadata and transcription text to file")
            return filename
        except Exception as e:
            print(f"[save_as_txt] Error occurred during processing of transcription: {filename}")
            print(f"[save_as_txt] Error message: {str(e)}")
            # print type of error
            print(f"[save_as_txt] Error type: {type(e)}")
            self.errors[filename] = str(e) # Store the error message in the dictionary
            return None

class myTranscriber:
    def __init__(self, model_size, errors=None, output=None):
        self.model = whisper.load_model(model_size)
        self.model_size = model_size
        self.errors = errors if errors is not None else {}
        self.output = output if output is not None else {}
        self.get_metadata = getMetadata()
        self.download_source = downloadSource()
        self.processed_videos_filename = 'data/processed-video-urls.txt'
        self.processed_videos = set()
        self._load_processed_videos()
    
    def _load_processed_videos(self):
        if not os.path.isfile(self.processed_videos_filename):
            open(self.processed_videos_filename, 'w').close()
        with open(self.processed_videos_filename, 'r') as file:
            for line in file:
                self.processed_videos.add(line.strip())
    
    # transcribe all videos in a channel
    def transcribe_channel(self, channel_url, channel_name):
        print(f"[transcribe_channel] Transcribing channel...{channel_name}")
        info_dict = self.get_metadata.get_channel_list(channel_url, channel_name, self.errors, self.output)
        if info_dict is None:
            return None
        limit = 60
        count = 0
        for video in info_dict['entries']:
            if video is not None and count <= limit:
                video_url = video['url']
                if video_url in self.processed_videos:
                    count += 1
                    print(f"[transcribe_channel] {colored(f'#{count}:', 'blue')} Skipping already processed video: {video_url}")
                    continue
                try:
                    result = self.transcribe_youtube_video(video['url'])
                    if result is None:
                        print(f"[transcribe_channel] Error occurred during transcription of video: {video_url}")
                    else:
                        print(f"DEBUG: transcribe result: {result}")
                        count += 1
                        print(f"[transcribe_channel] {colored(f'#{count}:', 'blue')} Completed processing video: {video_url}")
                    continue
                except Exception as e:
                    print(f"[transcribe_channel] Error occurred during transcription of video: {video_url}")
                    print(f"Error message: {str(e)}")
                    continue
        print(f"[transcribe_channel] Done transcribing channel {channel_name}")



    # transcribe a single video
    def transcribe_youtube_video(self, url, fp16=False, n=5, prefix='transcription'):
        try:
            # check if video has already been processed
            print(f"[transcribe_video] Checking if video was processed previously...{url}")
            if url in self.processed_videos:
                # ask user if they want to reprocess via the command line
                response = input(f"Video has already processed in a previous run. Do you want to reprocess? (y/n)")
                if response.lower() != 'y':
                    print(f"Skipping already processed video")
                    return f"Skipped video: {url}"
            
            print(f"[transcribe_video] downloading audio...{url}")
            filename = self.download_source.save_to_mp3(url)
            
            if(filename is None):
                # TODO: add url to error dictionary
                return None
            print(f"[transcribe_video] transcribing audio...using model: {colored(self.model_size, 'blue')}")
            text = self.model.transcribe(filename, fp16=fp16)
            print("[transcribe_video] Done transcribing audio")
            #print(f"DEBUG: [transcribe_video] Transcribed text obect: {text}")
            #print(f"DEBUG: [transcribe_video] First 20 characters of transcribed text: {text['text'][:20]}")
            splitter = myTextSplitter(text, n)
            
            # Get video metadata and append to dataframe
            #metadata = self.get_metadata.get_video_metadata(url)
            print(f"[transcribe_video] lookup url in saved metadata")
            metadata = self.get_metadata.channel_metadata.get(url, None)
            if metadata is None:
                print(f"[transcribe_video] saved meta not found - retrieving metadata from source")
                metadata = self.get_metadata.get_video_metadata(url)
            date = metadata['upload_date']  
            id = metadata['id']
            title = metadata['title'].replace(' ', '_').replace('/', '-')
            filepath = f'data/output/{prefix}-{date}-{title}-[{id}]-[model-{self.model_size}].txt'  

            # Save the modified dataframe as txt file
            processed_file = splitter.save_as_txt(filepath, metadata, self.model_size)
            if(processed_file is None):
                #TODO: add url to error dictionary
                return None
            else:
                print(f"[transcribe_video] Done transcribing video and saving to file")
                with open(self.processed_videos_filename, 'a') as file:
                    file.write(url + '\n')
                    print(f"[transcribe_video] Done adding video to processed-video-urls file [{self.processed_videos_filename}]"    )
                # add url to output dictionary
                self.output[url] = filepath
                return processed_file 

        
        except Exception as e:
            print(f"[transcribe_video] Error occurred during transcription of video: {url}")
            print(f"[transcribe_video] Error message: {str(e)}")
            self.errors[url] = str(e) # Store the error message in the dictionary
            return None
    def print_errors(self):
        print(colored("ERRORS:", "red"))
        pprint.pprint(self.errors)
    
    def print_output(self):
        print(colored("OUTPUT:", "blue"))
        pprint.pprint(self.output)

# create input and output directories
input_path = os.makedirs('data/input', exist_ok=True)
output_path = os.makedirs('data/output', exist_ok=True)

