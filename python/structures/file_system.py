from collections import defaultdict
from typing import List


class file_system:
    """
    Simple file system emulator. Extends my solution for leetcode problem #588:
    https://leetcode.com/problems/design-in-memory-file-system/

    In this implementation, files are stored separately from directories. File
    contents are stored as strings.

    Note: all path inputs begin with '/'.
    """

    def __init__(self):
        """
        Constructor for the file_system class.
        """
        self.files = defaultdict(str)
        self.directories = defaultdict(file_system)

    def __str__(self) -> str:
        """
        Creates string representation of the file system.

        System is represented as a horizontal tree, with each directory's
        contents sorted alphabetically.

        Returns
        -------
        str
            String representation of the file_system object.
        """
        file_strs = list(self.files.keys())
        dir_strs = []
        for dir_name, subdir in self.directories.items():
            dir_str = dir_name + '/'
            if not subdir._empty():
                dir_str += '\n\t' + '\n\t'.join(
                    line for line in str(subdir).split('\n')
                )
            dir_strs.append(dir_str)

        contents = sorted(file_strs + dir_strs)
        return '\n'.join(name for name in contents)

    def ls(self, path: str) -> List[str]:
        """
        Returns a sorted list of contents of the indicated path if it is a
        directory, returns the file name if it is a path.

        Parameters
        ----------
        path : str
            File path to be inspected.

        Returns
        -------
        List[str]
            Contents of the specified location if path is a directory, file
            name otherwise.

        Raises
        ------
        FileNotFoundError
            The path is invalid.
        """
        if path == '/':
            return sorted(
                list(self.files.keys()) + list(self.directories.keys())
            )

        curr, path_list = self, path[1:].split('/')

        for level in path_list[:-1]:
            if level not in curr.directories:
                raise FileNotFoundError(f'Invalid path: {path}')
            curr = curr.directories[level]

        if path_list[-1] in curr.files:
            return [path_list[-1]]
        elif path_list[-1] in curr.directories:
            curr = curr.directories[path_list[-1]]
            return sorted(
                list(curr.files.keys()) + list(curr.directories.keys())
            )
        else:
            raise FileNotFoundError(f'Invalid path: {path}')

    def mkdir(self, path: str):
        """
        Creates a new directory at the given path.

        Parameters
        ----------
        path : str
            Location at which to create a new directory.
        """
        curr_dir, path_list = self.directories, path[1:].split('/')

        for level in path_list:
            curr_dir = curr_dir[level].directories

    def add_content(self, path: str, content: str):
        """
        Appends new content to the contents of a specified file, or creates a
        new file if none exists.

        Parameters
        ----------
        path : str
            Location of the file.
        content : str
            Content to add to the file.
        """
        curr, path_list = self, path[1:].split('/')

        for level in path_list[:-1]:
            curr = curr.directories[level]

        curr.files[path_list[-1]] += content

    def cat(self, path: str) -> str:
        """
        Returns the contents of a file.

        Parameters
        ----------
        path : str
            Location of the file.

        Returns
        -------
        str
            The contents of the file.

        Raises
        ------
        FileNotFoundError
            The path is invalid.
        """
        curr, path_list = self, path[1:].split('/')

        for level in path_list[:-1]:
            if level not in curr.directories:
                raise FileNotFoundError(f'Invalid path: {path}')
            curr = curr.directories[level]

        if path_list[-1] not in curr.files:
            if path_list[-1] in curr.directories:
                raise FileNotFoundError(f'{path} is a directory')
            raise FileNotFoundError(f'File does not exist: {path}')
        return curr.files[path_list[-1]]

    def _empty(self) -> bool:
        """
        Determines if the file system is empty.

        Returns
        -------
        bool
            True if the file system contains no files or directories, False
            otherwise.
        """
        return len(self.files) + len(self.directories) == 0

    def rm(self, path: str, dir: bool = False, recursive: bool = False):
        """
        Removes the file or directory at the specified path.

        Parameters
        ----------
        path : str
            Target path to be deleted.
        dir : bool, optional
            Indicates target is a directory (defaults to False).
        recursive: bool, optional
            Indicates target can be deleted if nonempty (defaults to False).

        Raises
        ------
        FileNotFoundError
            Path is invalid.
        IsADirectoryError
            Target is a directory and dir is False.
        NotADirectoryError
            Target is a file and dir is True.
        PermissionError
            Target directory is nonempty and recursive is False.
        """
        curr, path_list = self, path[1:].split('/')
        final = path_list[-1]

        for level in path_list[:-1]:
            if level not in curr.directories:
                raise FileNotFoundError(f'Invalid path: {path}')
            curr = curr.directories[level]

        if final not in curr.files and final not in curr.directories:
            raise FileNotFoundError(f'Invalid path: {path}')

        if dir:
            if final in curr.files and final not in curr.directories:
                raise NotADirectoryError(f'{path} is not a directory')
            if not curr.directories[final]._empty() and not recursive:
                raise PermissionError(f'Directory not empty: {path}')
            curr.directories.pop(final)
        else:
            if final in curr.directories and final not in curr.files:
                raise IsADirectoryError(f'{path} is not a file')
            curr.files.pop(final)


def _system_from_str(file_str: str, file_contents: str = '') -> file_system:
    """
    Constructs a file system from its string representation.

    Parameters
    ----------
    file_str : str
        String representation of the file system.
    file_contents : str, optional
        String to create new files with (defaults to empty string).

    Returns
    -------
    file_system
        File system corresponding to the input string.
    """
    new_system = file_system()
    curr_dir, curr_str = None, ''
    for line in file_str.split('\n'):
        if not line.startswith('\t'):
            if line.endswith('/'):
                if curr_dir is not None:
                    new_system.directories[curr_dir] = _system_from_str(
                        file_str=curr_str,
                        file_contents=file_contents
                    )
                curr_dir, curr_str = line[:-1], ''
            else:
                new_system.files[line] = file_contents
        else:
            if curr_str:
                curr_str += '\n'
            curr_str += line[1:]

    if curr_dir is not None:
        new_system.directories[curr_dir] = _system_from_str(
            file_str=curr_str,
            file_contents=file_contents
        )

    return new_system
