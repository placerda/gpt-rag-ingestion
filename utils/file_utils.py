import os
import urllib.parse
from typing import Optional

def get_file_extension(file_path: str) -> Optional[str]:
    file_path = os.path.basename(file_path)
    return file_path.split(".")[-1].lower()

def get_filename(file_path: str) -> str:
    filename = file_path.rsplit('/', 1)[-1]
    return urllib.parse.unquote(filename)