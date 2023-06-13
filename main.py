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
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transcribe a YouTube video or channel.')
    subparsers = parser.add_subparsers(dest='command')
    help_model = '''
    Specifies Whisper model to use:
    Choices (english): [tiny.en, base.en, small.en, medium.en, large.v1, large.v2],
    Choices (multi-lingual): [base, medium, large.v1, large.v2]
    '''
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

    args = parser.parse_args()
    print(f"[main] args: {args}")
    # track errors by passing in a dictionary to transcriber
    errors = {}
    output = {}
    transcriber = myTranscriber(args.model if 'model' in args else 'tiny.en', errors, output)
    # added in aliases for commands - will not get recognized otherwise
    if args.command == 'list' or args.command == 'l':
        print(f"[main-generating channel list]: [{args.channel_name}] {args.channel_url}")
        transcriber.get_metadata.get_channel_list(args.channel_url, args.channel_name)
        if len(errors) > 0:
            print(f"[main-generating channel list]: complete - errors reported")
        else:
            print(f"[main-generating channel list]: complete")
    elif args.command == 'transcribe_channel' or args.command == 'tc':
        print(f"[main-transcribing channel]: {args.channel_url}")
        print(f"[main-transcribing channel]: {args}")
        print(f"[main-transcribing channel]: {args.model}")
        #transcriber.transcribe_channel(args.channel_url, args.channel_name, args.model)
        transcriber.transcribe_channel(args.channel_url, args.channel_name)
        if len(errors) > 0:
            print(f"[main-transcribing channel]: complete - errors reported")
        else:
            print(f"[main-transcribing channel]: complete")
    elif args.command == 'transcribe_video' or args.command == 'tv':
        print(f"[main-transcribing video]: {args.video_url}")
        print(f"[main-transcribing video]: {args}")
        transcriber.transcribe_youtube_video(args.video_url)
        if len(errors) > 0:
            print(f"[main-transcribing video]: complete - errors reported")
        else:
            print(f"[main-transcribing video]: complete")
    else:
        print(f"main-unknown command: {args.command}")
        parser.print_help()
    if len(output) > 0:
        transcriber.print_output()
    else:
        print(f"{colored('Output: ', 'blue')} None")
    if len(errors) > 0:
        transcriber.print_errors()

