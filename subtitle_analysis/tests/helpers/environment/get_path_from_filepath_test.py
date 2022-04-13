from ....source.helpers import environment

def test_path_from_filepath_returns_the_path():
    assert environment.get_path_from_filepath("/home/stho32/somefile.txt") == "/home/stho32"

