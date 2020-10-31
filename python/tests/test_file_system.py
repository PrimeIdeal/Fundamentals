import pytest

from python.structures.file_system import file_system


class TestFileSystem:
    """
    Test class for the file_system class.
    """

    @pytest.fixture(scope='class')
    def system(self):
        yield file_system()

    @pytest.mark.parametrize(
        'path, ls_path, expected',
        [
            ('/c', '/', ['c']),
            ('/b', '/', ['b', 'c']),
            ('/b/e', '/b', ['e']),
            ('/b/e', '/', ['b', 'c'])
        ],
        ids=[
            'One folder in root dir',
            'Two folders in root dir',
            'New folder one level down',
            'Check on root dir'
        ]
    )
    def test_mkdir(self, system, path, ls_path, expected):
        system.mkdir(path)
        assert system.ls(ls_path) == expected
