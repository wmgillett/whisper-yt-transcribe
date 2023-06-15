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
import logging
from utils import handle_error
#warnings.filterwarnings("ignore", category=DeprecationWarning, module='whisper.*')
warnings.filterwarnings("ignore", module='whisper.*')
logger = logging.getLogger(__name__)
class getMetadata:
    def __init__(self):   
        self.channel_metadata = {}
        
    # get channel list
    def get_channel_list(self, channel_url, channel_name, errors=None, output=None):
        func = '[get_channel_list]'
        errors = errors if errors is not None else {}
        output = output if output is not None else {}
        options = {
            'extract_flat': True,
        }
        try:
            with youtube_dl.YoutubeDL(options) as downloader:
                logger.info(f"{func} Getting channel list for {channel_name}...")
                info_dict = downloader.extract_info(channel_url, download=False)
                # save the urls in a txt file
                filename = f'data/channel_list_urls-[{channel_name}].txt' 
                logger.info(f"{func} Saving channel list urls to {filename}")
                # SKIP unless debugging
                json_string = json.dumps(info_dict, indent=4)
                logger.debug(f"{func} json_string: {json_string}")
                output[channel_url] = filename
                logger.debug(f"output: {output}")
                with open(filename, 'w') as f:
                    for entry in info_dict['entries']:
                        video_url = entry['url']
                        self.channel_metadata[video_url] = self.get_video_metadata(video_url)
                        f.write(video_url + '\n')
                logger.info(f"{func} Done getting channel list and saving to file {filename}")

            return info_dict
        except KeyError as e:
            #logger.error(f"{func} Error occurred during channel list generation for {channel_name}")
            msg = f"""
            Error occurred during channel list generation for {channel_name}
            Error related to missing key [entries] likely due to incorrect url for channel"
            """
            key = channel_url
            handle_error(e, func, msg, self.errors, key)
            return None
        except youtube_dl.utils.DownloadError as e:
            msg = f"""
            Download Error occurred during channel list generation for {channel_name}
            """
            key = channel_url
            errors = errors
            handle_error(e, func, msg, errors, key)
            return None
        except Exception as e:
            msg = f"""
            Unknown Error occurred during channel list generation for {channel_name}
            """
            key = channel_url
            handle_error(e, func, msg, self.errors, key)
            return None

    # get video metadata
    def get_video_metadata(self, url):
        func = '[get_video_metadata]'
        logger.info(f"{func} Starting process...{url}")
        options = {}
        try:
            with youtube_dl.YoutubeDL(options) as downloader:
                info_dict = downloader.extract_info(url, download=False)
                metadata = {
                    'url': url,
                    'title': info_dict.get('title'),
                    'description': info_dict.get('description'),
                    'channel': info_dict.get('channel'),
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
            msg = f"""
            Error occurred during metadata retrieval for {url}
            """
            key = url
            handle_error(e, func, msg, self.errors, key)
            return None
        logger.info(f"{func} Done getting video metadata")
        return metadata
    
class downloadSource:
    # download audio from youtube 
    def download_audio(self, url):
        func = '[download_audio]'
        logger.info(f"{func} Initiating download with youtube...{url}")
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
            logger.error(f"{func} Download failed")
            return None
        else:
            logger.info(f"{func} Done downloading")
            return download_file

    # call download source file as mp3 and save to data/input   
    def save_to_mp3(self, url):
        func = '[save_to_mp3]'
        logger.info(f"{func} calling download_audio...{url}")
        try:
            filename = self.download_audio(url)
        except youtube_dl.utils.DownloadError as e:
            msg = f"""
            Error occurred during download of {url}
            Like bad url or video not available
            """
            key = url
            handle_error(e, func, msg, self.errors, key)
            return None
        except Exception as e:
            msg = f"""
            2Error occurred during download of {url}
            Like bad url or video not available
            """
            key = url
            handle_error(e, func, msg, self.errors, key)
            return None
        if (filename is None):
            logger.error(f"{func} Download failed")
            return None
        else:
            filename = filename.replace('.m4a', '.mp3')
            logger.info(f"{func} Complete Filename: {filename}")
            return filename

class myTextSplitter:
    def __init__(self, text, n):
        self.text = text
        self.n = n

    def split_into_sentences(self):
        func = '[split_into_sentences]'
        logging.info(f"{func} splitting transcription into sentences")
        if self.text == "":
            raise ValueError("[split_into_sentences] Input text cannot be empty.")
        logger.debug(f"{func} self.text[:40]: {self.text['text'][:40]}")
        sentences = re.split("(?<=[.!?]) +", self.text['text'])
        logger.info(f"{func} Done splitting into sentences (n={len(sentences)})")
        return sentences

    def save_as_txt(self, filename, metadata, model):
        func = '[save_as_txt]'
        logger.info(f"{func} Formatting metadata and transcription text")
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
                    logger.info(f"{func} Saving sentences to txt file {filename}")
                    f.write(f'transcription model: {model}\n')
                    f.write(f'transcription text:\n')
                    for sentence in sentences:
                        f.write(sentence + '\n')
            logger.info(f"{func} Done saving metadata and transcription text to file")
            return filename
        except Exception as e:
            msg = "Error occurred during processing of transcription"
            key = filename
            handle_error(e, func, msg, self.errors, key)
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
        func = '[transcribe_channel]'
        logger.info(f"{func} Transcribing channel...{channel_name}")
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
                    logger.info(f"{func} {colored(f'#{count}:', 'blue')} Skipping already processed video: {video_url}")
                    continue
                try:
                    result = self.transcribe_youtube_video(video['url'])
                    if result is None:
                        logger.error(f"{func} Error occurred during transcription of video: {video_url}")
                    else:
                        logger.debug(f"{func} transcribe result: {result}")
                        count += 1
                        logger.info(f"{func} {colored(f'#{count}:', 'blue')} Completed processing video: {video_url}")
                    continue
                except Exception as e:
                    logger.error(f"{func} Error occurred during transcription of video: {video_url}")
                    logger.error(f"{func} Error message: {str(e)}")
                    continue
        logger.info(f"{func} Done transcribing channel {channel_name}")



    # transcribe a single video
    def transcribe_youtube_video(self, url, fp16=False, n=5, prefix='transcription'):
        func = '[transcribe_video]'
        try:
            # check if video has already been processed
            logger.info(f"{func} Checking if video was processed previously...{url}")
            if url in self.processed_videos:
                # ask user if they want to reprocess via the command line
                response = input(f"Video has already processed in a previous run. Do you want to reprocess? (y/n)")
                if response.lower() != 'y':
                    logger.info(f"{func} Skipping already processed video")
                    return f"Skipped video: {url}"
            
            logger.info(f"{func} downloading audio...{url}")
            filename = self.download_source.save_to_mp3(url)
            
            if(filename is None):
                # TODO: add url to error dictionary
                return None
            logger.info(f"{func} transcribing audio...using model: {colored(self.model_size, 'blue')}")
            text = self.model.transcribe(filename, fp16=fp16)
            logger.info(f"{func} Done transcribing audio")
            logger.debug(f"{func} Transcribed text[:40]: {text['text'][:40]}")
            splitter = myTextSplitter(text, n)
            
            # Get video metadata and append to dataframe
            #metadata = self.get_metadata.get_video_metadata(url)
            logger.info(f"{func} lookup url in saved metadata")
            metadata = self.get_metadata.channel_metadata.get(url, None)
            if metadata is None:
                logger.info(f"{func} saved meta not found - retrieving metadata from source")
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
                logger.info(f"{func} Done transcribing video and saving to file")
                with open(self.processed_videos_filename, 'a') as file:
                    file.write(url + '\n')
                    logger.info(f"{func} Done adding video to processed-video-urls file [{self.processed_videos_filename}]"    )
                # add url to output dictionary
                self.output[url] = filepath
                return processed_file 
        except Exception as e:
            msg = "Error occurred during transcription of video"
            handle_error(e, func, msg, self.errors, url)
            return None

# create input and output directories
input_path = os.makedirs('data/input', exist_ok=True)
output_path = os.makedirs('data/output', exist_ok=True)

