import pytest

from python.structures.trie import trie


class TestTrie:
    """
    Test class for the trie class.
    """

    @pytest.fixture(scope='class')
    def test_trie(self):
        yield trie()

    @pytest.mark.parametrize(
        'test_key',
        [
            'apple',
            '123',
            'xyz890'
        ],
        ids=[
            'Letters',
            'Numbers',
            'Letters and numbers'
        ]
    )
    def test_insert(self, test_trie, test_key):
        test_trie.insert(test_key)

        curr = test_trie
        for char in test_key:
            assert char in curr.children
            curr = curr.children[char]

        assert curr.children['key']

    @pytest.mark.parametrize(
        'test_key',
        [
            '@re',
            '',
            123
        ],
        ids=[
            'Not alphanumeric',
            'Empty string',
            'Not a string'
        ]
    )
    def test_insert_bad_input(self, test_trie, test_key):
        with pytest.raises(ValueError) as error_info:
            test_trie.insert(test_key)

        assert str(error_info.value) == f'Bad input: {test_key}'

    @pytest.mark.parametrize(
        'target, prefix, expected',
        [
            ('apple', False, True),
            ('xyz89', False, False),
            ('xyz', True, True),
            ('xyz', False, False),
            ('abc', True, False)
        ],
        ids=[
            'Key exists, prefix is False',
            'Key does not exist, prefix is False',
            'Prefix exists, prefix is True',
            'Prefix exists but key does not, prefix is False',
            'Prefix does not exist, prefix is True'
        ]
    )
    def test_search(self, test_trie, target, prefix, expected):
        assert test_trie.search(target, prefix) is expected

    @pytest.mark.parametrize(
        'target',
        [
            'C++',
            '',
            0
        ],
        ids=[
            'Not alphanumeric',
            'Empty string',
            'Not a string'
        ]
    )
    def test_search_bad_input(self, test_trie, target):
        with pytest.raises(ValueError) as error_info:
            test_trie.search(target)

        assert str(error_info.value) == f'Bad input: {target}'
