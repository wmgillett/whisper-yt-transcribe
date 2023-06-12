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
#warnings.filterwarnings("ignore", category=DeprecationWarning, module='whisper.*')
warnings.filterwarnings("ignore", module='whisper.*')

class getMetadata:
    # get channel list
    def get_channel_list(self, channel_url, channel_name):
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
                #print(f"[get_channel_list] info_dict: {info_dict}")
                json_string = json.dumps(info_dict, indent=4)
                print(f"DEBUG: json_string: {json_string[440000:489999]}")
                with open(filename, 'w') as f:
                    for entry in info_dict['entries']:
                        f.write(entry['url'] + '\n')
                print(f"[get_channel_list] Done getting channel list and saving to file {filename}")
            return info_dict
        # capture DownloadError exception
        except youtube_dl.utils.DownloadError as e:
            print(f"[get_channel_list] Download Error occurred during channel list generation for {channel_name}")
            print(f"[get_channel_list] Download Error message: {str(e)}")
            # get type of error 
            print(f"[get_channel_list] Error type: {type(e)}")
            return None
        except Exception as e:
            print(f"[get_channel_list] Error occurred during channel list generation for {channel_name}")
            print(f"[get_channel_list] Error message: {str(e)}")
            # get type of error 
            print(f"[get_channel_list] Error type: {type(e)}")
            return None

    # get video metadata
    def get_video_metadata(self, url):
        print(f"[get_video_metadata] Starting process...{url}")
        options = {}
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

    def save_as_txt(self, filename, metadata):
        print(f"[save_as_txt] Formatting audio transcription...{filename}")
        with open(filename, 'w') as f:
            if metadata is not None:
                for key, value in metadata.items():
                    f.write(f'{key}: {value}\n')
                f.write('\n')
            sentences = self.split_into_sentences()
            print(f"[save_as_txt] Saving sentences to txt file {filename}")
            for sentence in sentences:
                f.write(sentence + '\n')
        print("[save_as_txt] Done saving sentences to txt file")

    
class myTranscriber:
    def __init__(self, model_size):
        self.model = whisper.load_model(model_size)
        self.get_metadata = getMetadata()
        self.download_source = downloadSource()
    
    # transcribe all videos in a channel
    def transcribe_channel(self, channel_url, channel_name, model):
        print(f"[transcribe_channel] Transcribing channel...{channel_name}")
        info_dict = self.get_metadata.get_channel_list(channel_url, channel_name)
        limit = 60
        count = 0
        # Load the processed video URLs from the file
        processed_videos = set()
        processed_videos_filename = 'data/processed-video-urls.txt'
        # check if file exists and create if not
        if not os.path.isfile(processed_videos_filename):
            open(processed_videos_filename, 'w').close()
        with open(processed_videos_filename, 'r') as file:
            for line in file:
                processed_videos.add(line.strip())
        for video in info_dict['entries']:
            if video is not None and count <= limit:
                video_url = video['url']
                if video_url in processed_videos:
                    print(f"{count}: Skipping already processed video: {video_url}")
                    continue
                try:
                    self.transcribe_youtube_video(video['url'], model)
                    count += 1
                    # Append the processed video URL to the file
                    with open(processed_videos_filename, 'a') as file:
                        file.write(video_url + '\n')
                except Exception as e:
                    print(f"[transcribe_channel] Error occurred during transcription of video: {video_url}")
                    print(f"Error message: {str(e)}")
                    continue
        print(f"[transcribe_channel] Done transcribing channel {channel_name}")

    # transcribe a single video
    def transcribe_youtube_video(self, url, model, fp16=False, n=5, prefix='transcription'):
        try:
            print(f"[transcribe_video] downloading audio...{url}")
            filename = self.download_source.save_to_mp3(url)
            
            if(filename is None):
                return None
            print(f"[transcribe_video] Transcribing audio...using model {model}")
            text = self.model.transcribe(filename, fp16=fp16)
            print("[transcribe_video] Done transcribing audio")
            #print(f"DEBUG: [transcribe_video] Transcribed text obect: {text}")
            #print(f"DEBUG: [transcribe_video] First 20 characters of transcribed text: {text['text'][:20]}")
            splitter = myTextSplitter(text, n)
            
            # Get video metadata and append to dataframe
            metadata = self.get_metadata.get_video_metadata(url)
            #print(f"DEBUG: metadata: {metadata}")
            date = metadata['upload_date']  
            id = metadata['id']
            title = metadata['title'].replace(' ', '_').replace('/', '-')

            # Save the modified dataframe as txt file
            return splitter.save_as_txt(f'data/output/{prefix}-{date}-{title}-[{id}]-[model-{model}].txt', metadata)

        
        except Exception as e:
            print(f"[transcribe_video] Error occurred during transcription of video: {url}")
            print(f"[transcribe_video] Error message: {str(e)}")
            return None

# create input and output directories
input_path = os.makedirs('data/input', exist_ok=True)
output_path = os.makedirs('data/output', exist_ok=True)

