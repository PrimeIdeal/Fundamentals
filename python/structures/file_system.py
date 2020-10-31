from collections import defaultdict
from typing import List


class file_system:
    """
    Simple file system emulator. Solution for leetcode problem #588:
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
        else:
            curr = curr.directories[path_list[-1]]
            return sorted(
                list(curr.files.keys()) + list(self.directories.keys())
            )

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
            raise FileNotFoundError(f'File does not exist: {path}')
        return curr.files[path_list[-1]]
