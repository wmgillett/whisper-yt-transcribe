# transcripe-url.py
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

    def save_as_excel(self, filename):
        df = self.split_into_sentences_with_prompts()
        df.to_excel(filename, index=False)

    def save_as_csv(self, filename):
        df = self.split_into_sentences_with_prompts()
        df.to_csv(filename, index=False)
    def save_as_txt(self, filename):
        df = self.split_into_sentences_with_prompts()
        df.to_csv(filename, index=False,header=False)


    def save_as_json(self, filename):
        df = self.split_into_sentences_with_prompts()
        data = []
        for i in range(len(df)):
            row = {'prompt': df.iloc[i]['prompt'], 'completion': df.iloc[i]['completion']}
            data.append(row)
        with open(filename, 'w') as f:
            json.dump(data, f)



class myTranscriber:
    def __init__(self, model_size):
        self.model = whisper.load_model(model_size)
        
    def save_to_mp3(self, url):
        # getting bug using options
        #options = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio',
        #        'preferredcodec': 'mp3', 'preferredquality': '192'}]}
        options = {}
        print("Downloading audio...")
        with youtube_dl.YoutubeDL(options) as downloader:
            downloader.download([url])
        print("done downloading")
        print("Preparing mp3")
        #options = {'-k'}
        filename = downloader.prepare_filename(downloader.extract_info(url, download=False)).replace(".m4a", ".mp3")
        print(filename)
        return filename
        #return downloader.prepare_filename(downloader.extract_info(url, download=False)).replace(".m4a", ".mp3")

    def transcribe_youtube_video(self, url, fp16=False, n=5, op_name='transcribe2'):
        filename = self.save_to_mp3(url)
        text = self.model.transcribe(filename, fp16=fp16)
        splitter = myTextSplitter(text, n)
        splitter.save_as_txt(f'{op_name}.txt')
        return splitter.split_into_sentences_with_prompts()
# instantiate the transcriber with the whisper model
transcriber = myTranscriber("base")

transcription = transcriber.transcribe_youtube_video("https://www.youtube.com/watch?v=wGyTC5ygh1w")
# test with Rick Astley - Never Gonna Give You Up
#transcription = transcriber.transcribe_youtube_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")