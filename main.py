# main.py 
# this is the entry point for the program. 
# It parses command line arguments and calls the appropriate functions.
# Supported commands:
    # python main.py list CHANNEL_URL CHANNEL_NAME
    # python main.py transcribe_channel CHANNEL_URL CHANNEL_NAME --model medium.en
    # python main.py transcribe_video VIDEO_URL --model medium.en
import argparse
from transcribe_yt import myTranscriber, getMetadata, downloadSource
from termcolor import colored
import logging
import os
from utils import output_errors, output_output
import sys
from dotenv import load_dotenv
load_dotenv()


# setup logging
def setup_logging():
    log_level = os.getenv('LOG_LEVEL', 'DEBUG').upper()  # get log level from environment variable, default to 'DEBUG' if not found
    numeric_level = getattr(logging, log_level, None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {log_level}')
    log_format = os.getenv('LOG_FORMAT', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    print(f"log_format: {log_format}")
    logging.basicConfig(
        format=log_format,
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=numeric_level
    )
    logger = logging.getLogger(__name__)
    # Create file handler which logs info messages
    fh = logging.FileHandler('end_run.log')
    fh.setLevel(logging.INFO)

    # Create formatter and add it to the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(fh)

    # this code is not working - yt_dlp is still doing verbose logging
    yt_logger = logging.getLogger('yt_dlp')
    yt_logger.setLevel(logging.WARNING)

    return logger

def setup_parser():
    help_model = '''
    Specifies Whisper model to use:
    Choices (english): [tiny.en, base.en, small.en, medium.en, large.v1, large.v2],
    Choices (multi-lingual): [base, medium, large.v1, large.v2]
    '''
    parser = argparse.ArgumentParser(description='Transcribe a YouTube video or channel.')
    subparsers = parser.add_subparsers(dest='command')

    parser_list = subparsers.add_parser('list', aliases=['l'], help='Get a list of videos in a YouTube channel.')
    parser_list.add_argument('channel_url', type=str, help='The URL of the YouTube channel.')
    parser_list.add_argument('channel_name', type=str, help='The name of the YouTube channel.')

    parser_transcribe_channel = subparsers.add_parser('transcribe_channel', aliases=['tc'], help='Transcribe all videos in a YouTube channel.')
    parser_transcribe_channel.add_argument('channel_url', type=str, help='The URL of the YouTube channel.')
    parser_transcribe_channel.add_argument('channel_name', type=str, help='The name of the YouTube channel.') 
    parser_transcribe_channel.add_argument('-m', '--model', default='base.en', type=str, help=help_model)

    parser_transcribe_video = subparsers.add_parser('transcribe_video', aliases=['tv'], help='Transcribe a single YouTube video.')
    parser_transcribe_video.add_argument('video_url', type=str, help='The URL of the YouTube video.')
    parser_transcribe_video.add_argument('-m', '--model', default='base.en', type=str, help=help_model)

    return parser


def main():
    logger = setup_logging()
    parser = setup_parser()
    args = parser.parse_args()
     
    # create data dictionary of command to function mapping
    command_to_function = {
        'list': list_channel,
        'l': list_channel,
        'transcribe_channel': transcribe_channel,
        'tc': transcribe_channel,
        'transcribe_video': transcribe_video,
        'tv': transcribe_video
        }

    func = command_to_function.get(args.command)
    logger.debug(f"{func} args: {args}")
    if func:
        calling_func = func.__name__
        transcriber = myTranscriber(args.model if 'model' in args else 'tiny.en')

        if calling_func == 'list_channel':
            func(args, transcriber)
        else:
            func(args, transcriber)
        output_errors(transcriber.errors, calling_func)
        output_output(transcriber.output)
    else:
        print(f"[main] {colored(f'unknown command: ','red')}{args.command}")
        parser.print_help()   
        sys.exit(1)

def list_channel(args, transcriber):
        transcriber.get_metadata.get_channel_list(args.channel_url, args.channel_name, transcriber)

def transcribe_channel(args, transcriber):
        transcriber.transcribe_channel(args.channel_url, args.channel_name, transcriber)

def transcribe_video(args, transcriber):
        transcriber.transcribe_youtube_video(args.video_url)        


if __name__ == "__main__":
    main()