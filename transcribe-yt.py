# transcripe-yt.py
# script to use whisper to transcribe a url
import re
import pandas as pd
import whisper
import yt_dlp as youtube_dl
import json
import os

class myTextSplitter:
    def __init__(self, text, n):
        self.text = text
        self.n = n

    def split_into_sentences_with_prompts(self):
        #print(self.text)
        print(type(self.text))
        if self.text == "":
            raise ValueError("Input text cannot be empty.")
        if self.n <= 0:
            raise ValueError("n must be a positive integer.")
        sentences = re.split("(?<=[.!?]) +", self.text['text'])
        prompts = sentences[::self.n]
        completions = []
        for i in range(len(prompts) - 1):
            start = self.n * i
            end = min(self.n * (i + 1), len(sentences))
            completion = " ".join(sentences[start:end])
            completions.append(completion)
        completions.append(" ".join(sentences[self.n * (len(prompts) - 1) + 1:]))
        data = {'prompt': prompts, 'completion': completions}
        df = pd.DataFrame(data)
        return df
    
    def save_as_txt(self, filename, metadata=None):
        with open(filename, 'w') as f:
            if metadata is not None:
                for key, value in metadata.items():
                    f.write(f'{key}: {value}\n')
                f.write('\n')
            df = self.split_into_sentences_with_prompts()
            f.write(df.to_csv(index=False, header=False))
    
class myTranscriber:
    def __init__(self, model_size):
        self.model = whisper.load_model(model_size)

    # get channel list
    def get_channel_list(self, channel_url):
        options = {
            'extract_flat': True,
        }
        with youtube_dl.YoutubeDL(options) as downloader:
            print("Getting channel list...")
            info_dict = downloader.extract_info(channel_url, download=False)
            print("done getting channel list")
            # save the channel list as a json file
            with open('channel_list_entries.json', 'w') as f:
                json.dump(info_dict['entries'], f)
            # save the urls in a txt file
            with open('channel_list_urls.txt', 'w') as f:
                for entry in info_dict['entries']:
                    f.write(entry['url'] + '\n')
        return info_dict
    
    def transcribe_channel(self, channel_url):
        info_dict = self.get_channel_list(channel_url)
        limit = 60
        count = 0
        for video in info_dict['entries']:
            if video is not None and count <= limit:
                self.transcribe_youtube_video(video['url'])
                count += 1
    def get_video_metadata(self, url):
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
                # Add more fields as needed
            }
        return metadata
        
    def save_to_mp3(self, url):
        options = {}
        print("Downloading audio...")
        with youtube_dl.YoutubeDL(options) as downloader:
            downloader.download([url])
        print("done downloading")
        print("Preparing mp3")
        filename = downloader.prepare_filename(downloader.extract_info(url, download=False)).replace(".m4a", ".mp3")
        print(filename)
        return filename

    def transcribe_youtube_video(self, url, fp16=False, n=5, op_name='transcription'):
        filename = self.save_to_mp3(url)
        text = self.model.transcribe(filename, fp16=fp16)
        splitter = myTextSplitter(text, n)
        
        # Get video metadata and append to dataframe
        metadata = self.get_video_metadata(url)
        date = metadata['upload_date']
        title = metadata['title'].replace(' ', '_').replace('/', '-')
        # Save the modified dataframe as txt file
        splitter.save_as_txt(f'{op_name}_{date}_{title}.txt', metadata)
        return splitter.split_into_sentences_with_prompts()
    
# instantiate the transcriber with the whisper model
transcriber = myTranscriber("base")
#channel_list = transcriber.get_channel_list("https://www.youtube.com/@LynGenetThePlan/videos")
channel_list = transcriber.transcribe_channel("https://www.youtube.com/@LynGenetThePlan/videos")