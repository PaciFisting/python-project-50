from gendiff.scripts.gendiff import make_diff


def test_data():
    expected = '{\n' \
    '    - follow: False\n' \
    '      host: hexlet.io\n' \
    '    - proxy: 123.234.53.22\n' \
    '    - timeout: 50\n' \
    '    + timeout: 20\n' \
    '    + verbose: True\n' \
    '}'

    assert make_diff() == expected