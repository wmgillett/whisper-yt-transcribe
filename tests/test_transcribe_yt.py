# test_transcribe_yt.py

import pytest
#from unittest.mock import patch, MagicMock
from unittest.mock import Mock, patch, MagicMock
from transcribe_yt import myTranscriber, myTextSplitter, getMetadata, downloadSource

#@patch('transcribe_yt.myTranscriber.save_to_mp3')
#@patch('transcribe_yt.myTranscriber.save_to_mp3', return_value='mock_value')
#def test_save_to_mp3(mock_save_to_mp3):
    #transcriber = myTranscriber('tiny.en')  # assuming 'model_size' is a valid argument
    # Now when you call transcriber.save_to_mp3, it won't execute the real method, but will return 'mock_value' instead.
#def test_transcribe_youtube_video2():
#    transcriber = myTranscriber('tiny.en')  # assuming 'model_size' is a valid argument
#    transcriber.save_to_mp3 = MagicMock(return_value='mock_value')  # replace the instance method with a mock
    # call your function and check the results
#    result = transcriber.transcribe_youtube_video('https://youtu.be/dQw4w9WgXcQ', 'model') # Replace the URL and model with actual value
    # Assert the result
#    assert result is not None # change this to your actual assertion
@pytest.fixture
@patch('transcribe_yt.whisper.load_model')
def transcriber(mock_load_model):
    mock_load_model.return_value = Mock()
    return myTranscriber('tiny.en')
@pytest.fixture
def splitter():
    return myTextSplitter({'text': "Hello world! I am a transcriber."}, 5)
@pytest.fixture
def get_metadata():
    return getMetadata()
@pytest.fixture
def download_source():
    return downloadSource()

@patch('transcribe_yt.whisper.load_model')
def test_transcriber_initialization(mock_load_model):
    import sys
    print("sys.path:", sys.path) # Print out the Python path for debugging
    try:
        import whisper
        print("whisper module successfully imported!")
    except ImportError:
        print("Failed to import whisper module.")

    mock_load_model.return_value = Mock()
    transcriber = myTranscriber('tiny.en')
    
    mock_load_model.assert_called_once_with('tiny.en')
    assert transcriber.model is not None


# test get_channel_list
@patch('transcribe_yt.youtube_dl.YoutubeDL')
def test_get_channel_list(mock_youtube_dl, transcriber, get_metadata):
    mock_extractor = Mock()
    #mock_extractor.extract_info.return_value = {'entries': ['url1', 'url2']}
    mock_extractor.extract_info.return_value = {'entries': [{'url': 'url1'}, {'url': 'url2'}]}
    mock_youtube_dl.return_value.__enter__.return_value = mock_extractor

    # replace with a real channel URL for the test
    channel_url = "https://www.youtube.com/@RickAstleyYT/videos" 
    channel_name = "test_channel"
    info_dict = get_metadata.get_channel_list(channel_url, channel_name)

    assert info_dict is not None
    assert 'entries' in info_dict

# test video transcription
# setup transcription output
mock_transcribe = MagicMock()
mock_transcribe.transcribe.return_value = {
    "text": "This is a transcribed text. I'm gonna save goodbye",
    'segments': [
        {
            'id': 80,
            'seek': 19796,
            'start': 208.96,
            'end': 210.96,
            'text': "I'm gonna save goodbye",
            'tokens': [50913, 314, 1101, 8066, 3613, 24829, 51013],
            'temperature': 0.6,
            'avg_logprob': -0.35754344463348386,
            'compression_ratio': 1.6338028169014085,
            'no_speech_prob': 0.15678729116916656
        }
    ],
    'language': 'en'
}

@patch('transcribe_yt.whisper.load_model', return_value=mock_transcribe)
def test_transcribe_youtube_video(transcriber):
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    result = transcriber.transcribe_youtube_video(video_url)
    assert result is not None
    # buggy test - need to fix
    #result_invalid = transcriber.transcribe_youtube_video('https://youtu.be/INVALIDdQw4w9WgXcQ') 
    #assert result_invalid is None # 

@patch('transcribe_yt.youtube_dl.YoutubeDL')
def test_get_video_metadata(mock_youtube_dl, transcriber, get_metadata):
    mock_extractor = Mock()
    mock_extractor.extract_info.return_value = {
        'url': 'test_url', 'title': 'test_title', 'description': 'test_description',
        'uploader': 'test_uploader', 'upload_date': 'test_date', 'duration': 'test_duration',
        'view_count': 'test_views', 'like_count': 'test_likes', 'dislike_count': 'test_dislikes',
        'id': 'test_id', 'categories': 'test_categories', 'tags': 'test_tags'}
    mock_youtube_dl.return_value.__enter__.return_value = mock_extractor

    # replace with a real video URL for the test
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    metadata = get_metadata.get_video_metadata(video_url)

    assert metadata is not None
    assert 'url' in metadata
    assert 'title' in metadata
    assert 'description' in metadata
    assert 'uploader' in metadata
    assert 'upload_date' in metadata
    assert 'duration' in metadata
    assert 'view_count' in metadata
    assert 'like_count' in metadata
    assert 'id' in metadata
    assert 'categories' in metadata
    assert 'tags' in metadata

def test_split_into_sentences(splitter):
    sentences = splitter.split_into_sentences()

    assert len(sentences) == 2
    assert sentences[0] == "Hello world!"
    assert sentences[1] == "I am a transcriber."

# test downloadAudio
@patch('transcribe_yt.youtube_dl.YoutubeDL')
def test_download_audio(mock_youtube_dl, download_source):
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    filename = download_source.download_audio(video_url)

    assert filename is not None
    #assert os.path.isfile(filename)
    #os.remove(filename)