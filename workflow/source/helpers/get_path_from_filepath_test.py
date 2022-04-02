from .environment import get_path_from_filepath

def test_path_from_filepath_returns_the_path():
    assert get_path_from_filepath("/home/stho32/somefile.txt") == "/home/stho32"

