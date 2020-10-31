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

    @pytest.mark.parametrize(
        'path, content, ls_path, expected',
        [
            ('/a', 'A', '/', (['a', 'b', 'c'], 'A')),
            ('/b/e/f', 'F', '/b/e', (['f'], 'F')),
            ('/d/g', 'G', '/d', (['g'], 'G')),
            ('/a', '+', '/', (['a', 'b', 'c', 'd'], 'A+'))
        ],
        ids=[
            'New file in root dir',
            'New file in existing folder',
            'New file in new folder',
            'Append content to existing file'
        ]
    )
    def test_add_content(self, system, path, content, ls_path, expected):
        system.add_content(path, content)
        expected_ls, expected_cat = expected

        assert system.ls(ls_path) == expected_ls
        assert system.cat(path) == expected_cat
