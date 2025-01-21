import pytest
from fastapi import UploadFile
from app.utils.file_utils import verify_file_types, is_valid_file_size, MAX_FILE_SIZE, MAX_TOTAL_SIZE
from starlette.datastructures import Headers
from io import BytesIO

@pytest.fixture
def upload_file():
    def _upload_file(filename, content_type, size : int = 1):
        file = UploadFile(
            filename=filename, 
            file=BytesIO(b"test"),
            headers=Headers({"content-type": content_type}),
            size= size
        )
        return file
    return _upload_file

def test_verify_file_types_no_files():
    assert verify_file_types([]) == ("No files uploaded", None)

def test_verify_file_types_single_file(upload_file):
    file = upload_file("test.txt", "text/plain")
    assert verify_file_types([file]) == (None, "text/plain")

def test_verify_file_types_multiple_same_type_files(upload_file):
    file_1 = upload_file("test1.txt", "text/plain")
    file_2 = upload_file("test2.txt", "text/plain")
    assert verify_file_types([file_1, file_2]) == (None, "text/plain")

def test_verify_file_types_multiple_different_type_files(upload_file):
    file_1 = upload_file("test1.txt", "text/plain")
    file_2 = upload_file("test2.jpg", "image/jpeg")
    assert verify_file_types([file_1, file_2]) == ("All files must be of the same type", None)


def test_valid_file_sizes(upload_file):
    files = [upload_file("file1.txt", "text/plain", size=MAX_FILE_SIZE - 1),
             upload_file("file2.txt", "text/plain", size=MAX_FILE_SIZE - 1)]
    assert is_valid_file_size(files) == True

def test_single_file_exceeds_max_size(upload_file):
    files = [upload_file("file1.txt", "text/plain", size=MAX_FILE_SIZE + 1),
             upload_file("file2.txt", "text/plain", size=MAX_FILE_SIZE - 1)]
    assert is_valid_file_size(files) == False

def test_total_size_exceeds_max_size(upload_file):
    files = [ upload_file("file1.txt", "text/plain", size=MAX_TOTAL_SIZE // 2),
              upload_file("file2.txt", "text/plain", size=MAX_TOTAL_SIZE // 2)]
    assert is_valid_file_size(files) == False

def test_empty_file_list(upload_file):
    files = []
    assert is_valid_file_size(files) == False
