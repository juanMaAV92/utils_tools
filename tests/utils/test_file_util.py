import pytest
from fastapi import UploadFile
from app.utils.file_utils import verify_file_types
from starlette.datastructures import Headers
from io import BytesIO

@pytest.fixture
def upload_file():
    def _upload_file(filename, content_type):
        file = UploadFile(
            filename=filename, 
            file=BytesIO(b"test"), 
            headers=Headers({"content-type": content_type})
        )
        return file
    return _upload_file

def test_verify_file_types_no_files():
    assert verify_file_types([]) == ("No files uploaded", None)

def test_verify_file_types_single_file(upload_file):
    file = upload_file("test.txt", "text/plain")
    assert verify_file_types([file]) == (None, "text/plain")

def test_verify_file_types_multiple_same_type_files(upload_file):
    file1 = upload_file("test1.txt", "text/plain")
    file2 = upload_file("test2.txt", "text/plain")
    assert verify_file_types([file1, file2]) == (None, "text/plain")

def test_verify_file_types_multiple_different_type_files(upload_file):
    file1 = upload_file("test1.txt", "text/plain")
    file2 = upload_file("test2.jpg", "image/jpeg")
    assert verify_file_types([file1, file2]) == ("All files must be of the same type", None)