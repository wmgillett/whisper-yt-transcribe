# main.py 
# this is the entry point for the program. 
# It parses command line arguments and calls the appropriate functions.
# Supported commands:
    # python main.py list CHANNEL_URL CHANNEL_NAME
    # python main.py transcribe_channel CHANNEL_URL CHANNEL_NAME --model medium.en
    # python main.py transcribe_video VIDEO_URL --model medium.en
import argparse
from transcribe_yt import myTranscriber, getMetadata, downloadSource

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
    print(f"args: {args}")
    transcriber = myTranscriber(args.model if 'model' in args else 'tiny.en')
    # added in aliases for commands - will not get recognized otherwise
    if args.command == 'list' or args.command == 'l':
        print(f"[Generating channel list]: [{args.channel_name}] {args.channel_url}")
        transcriber.get_metadata.get_channel_list(args.channel_url, args.channel_name)
        print(f"[Generating channel list]: complete")
    elif args.command == 'transcribe_channel' or args.command == 'tc':
        print(f"[Transcribing channel]: {args.channel_url}")
        print(f"[Transcribing channel]: {args}")
        print(f"[Transcribing channel]: {args.model}")
        transcriber.transcribe_channel(args.channel_url, args.channel_name, args.model)
        print(f"[Transcribing channel]: complete")
    elif args.command == 'transcribe_video' or args.command == 'tv':
        print(f"[Transcribing video]: {args.video_url}")
        print(f"[Transcribing video]: {args}")
        transcriber.transcribe_youtube_video(args.video_url, args.model)
        print(f"[Transcribing video]: complete")
    else:
        print(f"Unknown command: {args.command}")
        parser.print_help()
