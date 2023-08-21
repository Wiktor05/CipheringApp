import pytest
import os
import json
from datetime import datetime
from src.files.file_handler import FileHandler

@pytest.fixture
def mock_datetime(monkeypatch):
    class MockDatetime:
        @classmethod
        def now(cls):
            return datetime(2023, 8, 20, 12, 0, 0) 

def test_save(tmpdir, mock_datetime):
    s = FileHandler('test_file.json')
    content = ['test content']
    s._save_rot13(content)
    expected_content = {
        "type": "ROT13",
        "content": content,
        "timestamp": "2023-08=20",
    }
    
    save_path = os.path.join(os.getcwd(), "content", "rot13", "2023-08-20-12:00:00.json")
    with open(save_path, "r") as file:
        saved_content = json.loads(file.read())

    assert saved_content == expected_content