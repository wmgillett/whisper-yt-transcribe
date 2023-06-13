import argparse
from transcribe_yt import myTranscriber  # import your classes/functions from transcribe-yt.py

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Transcribe a YouTube channel.')
    parser.add_argument('channel_url', type=str, help='The URL of the YouTube channel to transcribe.')
    parser.add_argument('-m', '--model_size', default='base', type=str, help='The size of the Whisper model to use.')

    args = parser.parse_args()

    transcriber = myTranscriber(args.model_size)
    transcriber.transcribe_channel(args.channel_url)
