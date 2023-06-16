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
mock_channel_info_dict, mock_video_info_dict

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
def test_get_channel_list_simple(mock_youtube_dl, transcriber, get_metadata):
    mock_extractor = Mock()
    mock_extractor.extract_info.return_value = {'entries': [{'url': 'url1'}, {'url': 'url2'}]}
    #mock_extractor.extract_info.return_value = json.loads(mock_channel_info_dict_valid)
    mock_youtube_dl.return_value.__enter__.return_value = mock_extractor

    channel_url = "https://www.youtube.com/@RickAstleyYT/videos" 
    channel_name = "test_channel"
    info_dict = get_metadata.get_channel_list(channel_url, channel_name, transcriber)
    assert info_dict is not None
    assert 'entries' in info_dict

@patch('transcribe_yt.youtube_dl.YoutubeDL')
def test_get_channel_list_standard(mock_youtube_dl, transcriber, get_metadata):
    mock_extractor = Mock()
    mock_extractor.extract_info.return_value = json.loads(mock_channel_info_dict)
    mock_youtube_dl.return_value.__enter__.return_value = mock_extractor

    # replace with a real channel URL for the test
    channel_url = "https://www.youtube.com/@RickAstleyYT/videos" 
    channel_name = "test_channel"
    info_dict = get_metadata.get_channel_list(channel_url, channel_name, transcriber)
    assert info_dict is not None
    assert 'entries' in info_dict

#@pytest.mark.skip(reason="json parsing error in mock data")
@patch('transcribe_yt.youtube_dl.YoutubeDL')
def test_get_channel_list_invalid(mock_youtube_dl, transcriber, get_metadata):
    mock_extractor = Mock()
    mock_extractor.extract_info.return_value = json.loads(mock_video_info_dict)
    mock_youtube_dl.return_value.__enter__.return_value = mock_extractor
    channel_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" 
    channel_name = "test_video-should-be-channel"
    info_dict = get_metadata.get_channel_list(channel_url, channel_name, transcriber)
    # update to function to return None if the channel metadata is invalid
    assert info_dict is None

# test video transcription
# setup transcription output
mock_transcribe = MagicMock()
@patch('transcribe_yt.whisper.load_model', return_value=mock_transcribe)
def test_transcribe_youtube_video_simple(transcriber):
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    result = transcriber.transcribe_youtube_video(video_url)
    mock_transcribe.transcribe.return_value = json.loads(mock_transcribed_text_simple)
    assert result is not None

mock_transcribe = MagicMock()
@patch('transcribe_yt.whisper.load_model', return_value=mock_transcribe)
def test_transcribe_youtube_video_complex(transcriber):
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    result = transcriber.transcribe_youtube_video(video_url)
    mock_transcribe.transcribe.return_value = json.loads(mock_transcribed_text_complex)
    assert result is not None

@patch('transcribe_yt.youtube_dl.YoutubeDL')
def test_get_video_metadata_simple(mock_youtube_dl, transcriber, get_metadata):
    mock_extractor = Mock()
    mock_extractor.extract_info.return_value = json.loads(mock_video_metadata_simple)
    mock_youtube_dl.return_value.__enter__.return_value = mock_extractor

    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    metadata = get_metadata.get_video_metadata(video_url, transcriber)

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

@patch('transcribe_yt.youtube_dl.YoutubeDL')
def test_get_video_metadata_complex(mock_youtube_dl, transcriber, get_metadata):
    mock_extractor = Mock()
    mock_extractor.extract_info.return_value = json.loads(mock_video_info_dict)
    mock_youtube_dl.return_value.__enter__.return_value = mock_extractor

    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    metadata = get_metadata.get_video_metadata(video_url, transcriber)

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

@patch('transcribe_yt.youtube_dl.YoutubeDL')
def test_get_video_metadata_invalid(mock_youtube_dl, transcriber, get_metadata):
    mock_extractor = Mock()
    mock_extractor.extract_info.return_value = json.loads(mock_channel_info_dict)
    mock_youtube_dl.return_value.__enter__.return_value = mock_extractor

    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    metadata = get_metadata.get_video_metadata(video_url, transcriber)

    assert metadata is None
    

def test_split_into_sentences(splitter):
    sentences = splitter.split_into_sentences()

    assert len(sentences) == 2
    assert sentences[0] == "Hello world!"
    assert sentences[1] == "I am a transcriber."

# test downloadAudio
@patch('transcribe_yt.youtube_dl.YoutubeDL')
def test_download_audio(mock_youtube_dl, download_source):
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    filename = download_source.download_audio(video_url, transcriber)

    assert filename is not None

# test_load_processed_videos
class TestLoadProcessedVideos:
    filename = "test_processed_videos.txt"
    def setup_method(self):
        # run before each test method
        self.transcriber = myTranscriber('tiny.en')
        self.transcriber.processed_videos_filename = self.filename
        self.transcriber.processed_videos.clear()
    def teardown_method(self):
        # run after each test method
        if os.path.exists(self.filename):
            os.unlink(self.filename)
    
    def test_file_does_not_exist(self):
        self.transcriber._load_processed_videos()
        # checking that a new file is created
        assert os.path.isfile(self.filename)
        # confirming that the file is empty
        assert not self.transcriber.processed_videos

    def test_file_exists(self):
        video_ids = ["test_video_id1", "test_video_id2", "test_video_id3"]
        with open(self.filename, "w") as f:
            for video_id in video_ids:
                f.write(video_id + "\n")
        self.transcriber._load_processed_videos()
        assert self.transcriber.processed_videos == set(video_ids)            
