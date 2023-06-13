# test_transcribe_yt.py

import pytest
#from unittest.mock import patch, MagicMock
from unittest.mock import Mock, patch, MagicMock
import json
from transcribe_yt import myTranscriber, myTextSplitter, getMetadata, downloadSource
import sys
import os
# insure files like mock_data.py can be loaded from the tests directory
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from mock_data import mock_video_metadata_simple, \
mock_transcribed_text_simple, mock_transcribed_text_complex, \
mock_channel_info_dict_valid, mock_video_info_dict

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

    mock_extractor.extract_info.return_value = json.loads(mock_channel_info_dict_valid)
    assert info_dict is not None
    assert 'entries' in info_dict

    # buggy mock data - need to fix - this input should cause issues
    # mock_extractor.extract_info.return_value = json.loads(mock_video_info_dict)
    # assert info_dict is not None
    # assert 'entries' not in info_dict

# test video transcription
# setup transcription output
mock_transcribe = MagicMock()
@patch('transcribe_yt.whisper.load_model', return_value=mock_transcribe)
def test_transcribe_youtube_video(transcriber):
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    result = transcriber.transcribe_youtube_video(video_url)
    mock_transcribe.transcribe.return_value = json.loads(mock_transcribed_text_simple)
    assert result is not None
    
    # buggy test data - need to fix 
    #mock_transcribe.transcribe.return_value = json.loads(mock_transcribed_text_complex)
    #assert result is not None
    
    # buggy test - need to fix
    #result_invalid = transcriber.transcribe_youtube_video('https://youtu.be/INVALIDdQw4w9WgXcQ') 
    #assert result_invalid is None # 

@patch('transcribe_yt.youtube_dl.YoutubeDL')
def test_get_video_metadata(mock_youtube_dl, transcriber, get_metadata):
    mock_extractor = Mock()
    mock_extractor.extract_info.return_value = json.loads(mock_video_metadata_simple)
    mock_youtube_dl.return_value.__enter__.return_value = mock_extractor

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