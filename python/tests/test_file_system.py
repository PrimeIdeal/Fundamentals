import pytest

from python.structures.file_system import file_system


class TestFileSystem:
    """
    Test class for the file_system class.
    """

    @pytest.fixture(scope='class')
    def test_system(self):
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
    def test_mkdir(self, test_system, path, ls_path, expected):
        test_system.mkdir(path)

        assert test_system.ls(ls_path) == expected

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
    def test_add_content(self, test_system, path, content, ls_path, expected):
        test_system.add_content(path, content)
        expected_ls, expected_cat = expected

        assert test_system.ls(ls_path) == expected_ls
        assert test_system.cat(path) == expected_cat

    @pytest.mark.parametrize(
        'path, expected',
        [
            ('/', ['a', 'b', 'c', 'd']),
            ('/a', ['a']),
            ('/d', ['g']),
            ('/d/g', ['g'])
        ],
        ids=[
            'Root dir',
            'File in root dir',
            'Folder one level down',
            'File one level down'
        ]
    )
    def test_ls(self, test_system, path, expected):
        assert test_system.ls(path) == expected

    @pytest.mark.parametrize(
        'path, error_msg',
        [
            ('/r/q', 'Invalid path: /r/q'),
            ('/d/u', 'Invalid path: /d/u')
        ],
        ids=[
            'Invalid intermediate component of path',
            'Invalid final component of path'
        ]
    )
    def test_ls_bad_path(self, test_system, path, error_msg):
        with pytest.raises(FileNotFoundError) as error_info:
            test_system.ls(path)

        assert(str(error_info.value)) == error_msg

    @pytest.mark.parametrize(
        'path, expected',
        [
            ('/a', 'A+'),
            ('/b/e/f', 'F')
        ],
        ids=[
            'File in root dir',
            'File in subdirs'
        ]
    )
    def test_cat(self, test_system, path, expected):
        assert test_system.cat(path) == expected
