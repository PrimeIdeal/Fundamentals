import pytest

from python.structures.linked_list import linked_list


class TestLinkedList:
    """
    Test class for the linked_list class.
    """

    @pytest.mark.parametrize(
        'nodes, expected',
        [
            ([1, 2, 3], [1, 2, 3]),
            ([None], [None]),
            ([None, 3], [None, 3]),
            ([], []),
            (None, [])
        ],
        ids=[
            'No Nulls',
            'Null values in list',
            'Null and non-null',
            'Empty input',
            'Null input'
        ]
    )
    def test_serialize(self, nodes, expected):
        test_list = linked_list(nodes)

        assert test_list.serialize() == expected

    @pytest.mark.parametrize(
        'nodes, expected',
        [
            ([1, 2, 3], '[1->2->3]'),
            ([], '[]'),
            ([None, 3], '[None->3]')
        ],
        ids=[
            'No Nulls',
            'Empty list',
            'List with Nulls'
        ]
    )
    def test_str(self, nodes, expected):
        test_list = linked_list(nodes)

        assert str(test_list) == expected

    @pytest.mark.parametrize(
        'nodes1, nodes2',
        [
            ([1, 2, 3], [1, 2, 3]),
            pytest.param([], [None], marks=pytest.mark.xfail),
            pytest.param([1, 2, 3], [3, 2, 1], marks=pytest.mark.xfail),
            pytest.param([1, 2], [1, 2, 3], marks=pytest.mark.xfail)
        ],
        ids=[
            'No Nulls',
            'Empty and null inputs',
            'Reversed list',
            'Different lengths'
        ]
    )
    def test_eq(self, nodes1, nodes2):
        test_list1 = linked_list(nodes1)
        test_list2 = linked_list(nodes2)

        assert test_list1 == test_list2

    @pytest.mark.parametrize(
        'nodes, val, expected',
        [
            ([1, 2, 3], 3, [3]),
            ([1, 2, 3], 2, [2, 3]),
            ([1, 2, 3], 4, None)
        ],
        ids=[
            'Node exists - no next node',
            'Node exists - next node',
            'Node does not exist'
        ]
    )
    def test_get_node(self, nodes, val, expected):
        test_list = linked_list(nodes)
        if expected is not None:
            expected_list = linked_list(expected)
            assert test_list.get_node(val) == expected_list
        else:
            assert test_list.get_node(val) == expected

    @pytest.mark.parametrize(
        'nodes, expected',
        [
            ([1, 2, 3], [3]),
            ([1, 2, None], [None]),
            ([], [])
        ],
        ids=[
            'Nonempty list',
            'Nonempty list - Null tail',
            'Empty list'
        ]
    )
    def test_get_tail(self, nodes, expected):
        test_list = linked_list(nodes)
        expected_node = linked_list(expected)

        assert test_list.get_tail() == expected_node

    @pytest.mark.parametrize(
        'nodes, val, expected',
        [
            ([1, 2, 3], 0, [0, 1, 2, 3]),
            ([], 0, [0])
        ],
        ids=[
            'Nonempty list',
            'Empty list'
        ]
    )
    def test_insert_head(self, nodes, val, expected):
        test_list = linked_list(nodes)
        expected_list = linked_list(expected)

        test_list = test_list.insert_head(val)

        assert test_list == expected_list
