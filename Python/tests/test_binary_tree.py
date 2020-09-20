import pytest


from Python.structures.binary_tree import (
    binary_search_tree,
    binary_tree
)


class TestBinaryTree:
    """
    Test class for the binary_tree class.
    """

    def test_equal(self):
        node_list = [5,
                     [12, [9, None, None], [3, None, None]],
                     [17, None, [2, None, None]]]
        test_tree1 = binary_tree(node_list)
        test_tree2 = binary_tree(node_list)

        assert test_tree1 == test_tree2

    def test_str(self):
        node_list = [5,
                     [12, [9, None, None], [3, None, None]],
                     [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)
        result = '[5,[12,[9,None,None],[3,None,None]],[17,None,[2,None,None]]]'

        assert str(test_tree) == result

    def test_serialize(self):
        node_list = [5,
                     [12, [9, None, None], [3, None, None]],
                     [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)

        assert test_tree.serialize() == node_list

    def test_preorder_traversal(self):
        node_list = [5,
                     [12, [9, None, None], [3, None, None]],
                     [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)

        assert test_tree.preorder_traversal() == [5, 12, 9, 3, 17, 2]

    def test_inorder_traversal(self):
        node_list = [5,
                     [12, [9, None, None], [3, None, None]],
                     [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)

        assert test_tree.inorder_traversal() == [9, 12, 3, 5, 17, 2]

    def test_postorder_traversal(self):
        node_list = [5,
                     [12, [9, None, None], [3, None, None]],
                     [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)

        assert test_tree.postorder_traversal() == [9, 3, 12, 2, 17, 5]

    def test_verify_bst(self):
        node_list1 = [5,
                      [12, [9, None, None], [3, None, None]],
                      [17, None, [2, None, None]]]
        node_list2 = [12,
                      [5, [2, None, None], [9, None, None]],
                      [17, [14, None, None], None]]
        test_tree1 = binary_tree(node_list1)
        test_tree2 = binary_tree(node_list2)

        assert not test_tree1.verify_bst()
        assert test_tree2.verify_bst()

    def test_breadth_first_search(self):
        node_list = [5,
                     [12, [9, None, None], [3, None, None]],
                     [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)

        assert test_tree.breadth_first_search(3)
        assert not test_tree.breadth_first_search(14)

    def test_breadth_first_search_retrieval(self):
        node_list = [5,
                     [12, [9, None, None], [3, None, None]],
                     [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)
        result_list = [17, None, [2, None, None]]
        result_tree = binary_tree(result_list)

        assert test_tree.breadth_first_search(17, retrieve=True) == result_tree
        assert test_tree.breadth_first_search(1, retrieve=True) is None

    def test_depth_first_search(self):
        node_list = [5,
                     [12, [9, None, None], [3, None, None]],
                     [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)

        assert test_tree.depth_first_search(3)
        assert not test_tree.depth_first_search(14)

    def test_depth_first_search_retrieval(self):
        node_list = [5,
                     [12, [9, None, None], [3, None, None]],
                     [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)
        result_list = [17, None, [2, None, None]]
        result_tree = binary_tree(result_list)

        assert test_tree.depth_first_search(17, retrieve=True) == result_tree
        assert test_tree.depth_first_search(1, retrieve=True) is None

    def test_invert(self):
        node_list = [5,
                     [12, [9, None, None], [3, None, None]],
                     [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)
        inverted_list = [5,
                         [17, [2, None, None], None],
                         [12, [3, None, None], [9, None, None]]]
        inverted_tree = binary_tree(inverted_list)

        assert test_tree.invert() == inverted_tree


class TestBST:
    """
    Test class for the binary_search_tree class.
    """

    def test_min(self):
        node_list = [12,
                     [5, [2, None, None], [9, None, None]],
                     [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)

        assert test_tree.minimum() == 2

    def test_max(self):
        node_list = [12,
                     [5, [2, None, None], [9, None, None]],
                     [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)

        assert test_tree.maximum() == 17

    def test_search(self):
        node_list = [12,
                     [5, [2, None, None], [9, None, None]],
                     [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)

        assert test_tree.search(9, retrieve=False)
        assert not test_tree.search(-3, retrieve=False)

    def test_search_retrieval(self):
        node_list = [12,
                     [5, [2, None, None], [9, None, None]],
                     [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)
        result_list = [5,
                       [2, None, None],
                       [9, None, None]]
        result_tree = binary_search_tree(result_list)

        assert test_tree.search(5, retrieve=True) == result_tree
        assert test_tree.search(7, retrieve=True) is None

    def test_search_empty_tree(self):
        test_tree = binary_search_tree()

        assert not test_tree.search(7)

    def test_successor(self):
        node_list = [12,
                     [5, [2, None, None], [9, None, None]],
                     [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)

        assert test_tree.successor(5) == 9
        assert test_tree.successor(9) == 12
        assert test_tree.successor(17) is None

    def test_predecessor(self):
        node_list = [12,
                     [5, [2, None, None], [9, None, None]],
                     [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)

        assert test_tree.predecessor(5) == 2
        assert test_tree.predecessor(14) == 12
        assert test_tree.predecessor(2) is None

    def test_insert(self):
        node_list = [12,
                     [5, [2, None, None], [9, None, None]],
                     [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)
        result_list = [12,
                       [5, [2, None, None], [9, None, None]],
                       [17, [14, None, [15, None, None]], None]]
        result_tree = binary_search_tree(result_list)

        test_tree.insert(15)

        assert test_tree == result_tree

    def test_insert_empty_tree(self):
        test_tree = binary_search_tree(node_list=None)
        test_tree.insert(7)
        result_tree = binary_search_tree([7, None, None])

        assert test_tree == result_tree

    def test_transplant(self):
        node_list = [12,
                     [5, [2, None, None], [9, None, None]],
                     [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)
        result_list = [12,
                       [5, [2, None, None], [17, [14, None, None], None]],
                       [17, [14, None, None], None]]
        result_tree = binary_search_tree(result_list)

        to_replace = test_tree.search(9, retrieve=True)
        replacement = test_tree.search(17, retrieve=True)
        test_tree.transplant(to_replace, replacement)

        assert test_tree == result_tree

    def test_distance(self):
        node_list = [12,
                     [5, [2, None, None], [9, None, None]],
                     [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)

        assert test_tree.distance(14, 5) == 3
        assert test_tree.distance(5, 2) == 1

    def test_distance_one_nonexistent(self):
        node_list = [12,
                     [5, [2, None, None], [9, None, None]],
                     [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)

        with pytest.raises(ValueError) as error_info:
            test_tree.distance(15, 2)

        assert '15 does not exist in the tree.' in str(error_info)

    def test_distance_both_nonexistent(self):
        node_list = [12,
                     [5, [2, None, None], [9, None, None]],
                     [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)

        with pytest.raises(ValueError) as error_info:
            test_tree.distance(15, 1)

        assert '15 and 1 do not exist in the tree' in str(error_info)
