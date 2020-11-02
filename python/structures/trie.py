from collections import defaultdict


class trie:
    """
    A search tree where the value of the key is distributed across the
    structure.

    Keys are alphanumeric strings in this implementation.
    """

    def __init__(self):
        """
        Constructor for the trie class.
        """
        self.children = defaultdict(trie)

    def insert(self, new_key: str):
        """
        Inserts a new key into the trie.

        Parameters
        ----------
        new_key : str
            Key to be inserted into trie.

        Raises
        ------
        ValueError
            New key contains non-alphanumeric characters or is empty.
        """
        if not isinstance(new_key, str) or not new_key.isalnum():
            raise ValueError(f'Bad input: {new_key}')

        curr = self
        for char in new_key:
            curr = curr.children[char]

        curr.children['key'] = True

    def search(self, target: str, prefix: bool = False) -> bool:
        """
        Searches for the target string in the trie.

        Parameters
        ----------
        target : str
            String to search for.
        prefix : str, optional
            Indicates target is a prefix (defaults to False).

        Returns
        -------
        bool
            True if target is a key (or prefix) in the trie, False otherwise.

        Raises
        ------
        ValueError
            Target string contains non-alphanumeric characters or is empty.
        """
        if not isinstance(target, str) or not target.isalnum():
            raise ValueError(f'Bad input: {target}')

        curr = self
        for char in target:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        if 'key' not in curr.children and not prefix:
            return False
        return True
