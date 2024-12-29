from typing import List, Optional, Tuple

from fastapi import UploadFile


def verify_file_types(files: List[UploadFile]) -> Tuple[Optional[str], Optional[str]]:
    if not files:
        return "No files uploaded", None

    first_file_type = files[0].content_type

    for file in files:
        if file.content_type != first_file_type:
            return "All files must be of the same type", None

    return None, first_file_type
