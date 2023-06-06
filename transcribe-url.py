# transcripe-url.py
# script to use whisper to transcribe a url
import whisper
# import youtube_dl
# trying new fork as youtube_dl is not working
# https://github.com/yt-dlp/yt-dlp
import yt_dlp as youtube_dl
#import yt_dlp
import os

class myTranscriber:
    def __init__(self, model_size):
        self.model = whisper.load_model(model_size)
        
    def save_to_mp3(self, url):
        options_org = {'format': 'bestaudio/best', 'postprocessors': [{'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3', 'preferredquality': '192'}]}
        options = {}
        with youtube_dl.YoutubeDL(options) as downloader:
            downloader.download([url])

        return downloader.prepare_filename(downloader.extract_info(url, download=False)).replace(".m4a", ".mp3")

    def transcribe_youtube_video(self, url, fp16=False, n=5, op_name='transcribe'):
        filename = self.save_to_mp3(url)
        text = self.model.transcribe(filename, fp16=fp16)
        write_file = open("transcription.txt", "w")
        write_file.write(text)
        return text
# instantiate the transcriber with the whisper model
transcriber = myTranscriber("base")

#transcription = transcriber.transcribe_youtube_video("https://www.youtube.com/watch?v=wGyTC5ygh1w")
transcription = transcriber.transcribe_youtube_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")