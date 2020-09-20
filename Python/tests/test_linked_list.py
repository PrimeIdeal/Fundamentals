import pytest

from Python.structures.linked_list import linked_list


class TestLinkedList:
    """
    Test class for the linked_list class.
    """

    @pytest.mark.parametrize(
        'node_list, expected',
        [
            ([1, 2, 3], [1, 2, 3]),
            ([None], [None]),
            ([None, 3], [None, 3]),
            ([], [None])
        ]
    )
    def test_serialize(self, node_list, expected):
        test_list = linked_list(node_list=node_list)

        assert test_list.serialize() == expected
