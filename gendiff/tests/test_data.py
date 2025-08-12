from pathlib import Path
from gendiff.scripts.gendiff import main

def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename

def read_file(filename):
    return get_test_data_path(filename).read_text()

def test_comparison():
    expected = '{' \
    '  - follow: False' \
    '  host: hexlet.io' \
    '  - proxy: 123.234.53.22' \
    '  - timeout: 50' \
    '  + timeout: 20' \
    '  + verbose: True' \
    '}'