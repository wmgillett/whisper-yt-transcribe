# transcribe-yt.py
# script to use whisper to transcribe youtube videos
import re
import pandas as pd
import whisper
import yt_dlp as youtube_dl
import json
import os
import warnings
#warnings.filterwarnings("ignore", category=DeprecationWarning, module='whisper.*')
warnings.filterwarnings("ignore", module='whisper.*')

class myTextSplitter:
    def __init__(self, text, n):
        self.text = text
        self.n = n

    def split_into_sentences(self):
        print("Splitting transcription into sentences")
        if self.text == "":
            raise ValueError("Input text cannot be empty.")
        print(f"self.text: {self.text}")
        print(f"First 20 characters of text: {self.text['text'][:20]}")
        sentences = re.split("(?<=[.!?]) +", self.text['text'])
        print(f"Done splitting into sentences (n={len(sentences)})")
        return sentences

    def save_as_txt(self, filename, metadata):
        print(f"Formatting audio transcription...{filename}")
        with open(filename, 'w') as f:
            if metadata is not None:
                for key, value in metadata.items():
                    f.write(f'{key}: {value}\n')
                f.write('\n')
            sentences = self.split_into_sentences()
            print(f"Saving sentences to txt file {filename}")
            for sentence in sentences:
                f.write(sentence + '\n')
        print("Done saving sentences to txt file")

    
class myTranscriber:
    def __init__(self, model_size):
        self.model = whisper.load_model(model_size)

    # get channel list
    def get_channel_list(self, channel_url, channel_name):
        options = {
            'extract_flat': True,
        }
        with youtube_dl.YoutubeDL(options) as downloader:
            print(f"Getting channel list for {channel_name}...")
            info_dict = downloader.extract_info(channel_url, download=False)
            # save the urls in a txt file
            filename = f'data/channel_list_urls-[{channel_name}].txt' 
            print(f"Saving channel list urls to {filename}")
            with open(filename, 'w') as f:
                for entry in info_dict['entries']:
                    f.write(entry['url'] + '\n')
            print(f"Done getting channel list and saving to file {filename}")
        return info_dict
    
    # transcribe all videos in a channel
    def transcribe_channel(self, channel_url, channel_name, model):
        info_dict = self.get_channel_list(channel_url, channel_name)
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
                    print(f"Error occurred during transcription of video: {video_url}")
                    print(f"Error message: {str(e)}")
                    continue

    # get video metadata
    def get_video_metadata(self, url):
        print("Getting video metadata...")
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
        print("Done getting video metadata")
        return metadata
    
    # save to source file as mp3 and into data/input
    def save_to_mp3(self, url):
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
        print("Downloading audio...")
        with youtube_dl.YoutubeDL(options) as downloader:
            downloader.download([url])
        print("Done downloading")
        print("Preparing mp3")
        filename = downloader.prepare_filename(downloader.extract_info(url, download=False)).replace(".webm", ".mp3")
        filename = filename.replace('.m4a', '.mp3')
        print(f"Filename: {filename}")
        print("Done preparing mp3")
        return filename


    def transcribe_youtube_video(self, url, model, fp16=False, n=5, prefix='transcription'):
        print(f"Transcribing video...{url}")
        try:
            filename = self.save_to_mp3(url)
            print(f"Transcribing audio...using model {model}")
            text = self.model.transcribe(filename, fp16=fp16)
            print("Done transcribing audio")
            print(f"Transcribed text obect: {text}")
            # print first 20 characters of text
            print(f"DEBUG: First 20 characters of transcribed text: {text['text'][:20]}")
            splitter = myTextSplitter(text, n)
            
            # Get video metadata and append to dataframe
            metadata = self.get_video_metadata(url)
            print(f"metadata: {metadata}")
            date = metadata['upload_date']  
            id = metadata['id']
            title = metadata['title'].replace(' ', '_').replace('/', '-')

            # Save the modified dataframe as txt file
            return splitter.save_as_txt(f'data/output/{prefix}-{date}-{title}-[{id}]-[model-{model}].txt', metadata)

        
        except Exception as e:
            print(f"Error occurred during transcription of video: {url}")
            print(f"Error message: {str(e)}")
            return None

# create input and output directories
input_path = os.makedirs('data/input', exist_ok=True)
output_path = os.makedirs('data/output', exist_ok=True)

