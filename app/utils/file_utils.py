from typing import List, Optional, Tuple

from fastapi import UploadFile


MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 MB por archivo
MAX_TOTAL_SIZE = 20 * 1024 * 1024  # 20 MB en total


def verify_file_types(files: List[UploadFile]) -> Tuple[Optional[str], Optional[str]]:
    if not files:
        return "No files uploaded", None

    first_file_type = files[0].content_type

    for file in files:
        if file.content_type != first_file_type:
            return "All files must be of the same type", None

    return None, first_file_type


def is_valid_file_size(files: List[UploadFile]) -> bool:

    if not files:
        return False

    total_size = 0

    for file in files:
        if file.size > MAX_FILE_SIZE:
            return False
        total_size += file.size
        if total_size > MAX_TOTAL_SIZE:
            return False

    return True