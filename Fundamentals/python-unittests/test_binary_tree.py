import unittest

from structures.binary_tree import binary_search_tree, binary_tree


class test_binary_tree(unittest.TestCase):

    def test_equal(self):
        node_list = [5, [12, [9, None, None], [3, None, None]], [17, None, [2, None, None]]]
        test_tree1 = binary_tree(node_list)
        test_tree2 = binary_tree(node_list)

        self.assertEqual(test_tree1, test_tree2)

    def test_str(self):
        node_list = [5, [12, [9, None, None], [3, None, None]], [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)

        self.assertEqual(str(test_tree), '[5, [12, [9, None, None], [3, None, None]], [17, None, [2, None, None]]]')

    def test_serialize(self):
        node_list = [5, [12, [9, None, None], [3, None, None]], [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)

        self.assertEqual(test_tree.serialize(), node_list)

    def test_preorder_traversal(self):
        node_list = [5, [12, [9, None, None], [3, None, None]], [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)

        self.assertEqual(test_tree.preorder_traversal(), [5, 12, 9, 3, 17, 2])

    def test_inorder_traversal(self):
        node_list = [5, [12, [9, None, None], [3, None, None]], [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)

        self.assertEqual(test_tree.inorder_traversal(), [9, 12, 3, 5, 17, 2])

    def test_postorder_traversal(self):
        node_list = [5, [12, [9, None, None], [3, None, None]], [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)

        self.assertEqual(test_tree.postorder_traversal(), [9, 3, 12, 2, 17, 5])

    def test_verify_bst(self):
        node_list1 = [5, [12, [9, None, None], [3, None, None]], [17, None, [2, None, None]]]
        node_list2 = [12, [5, [2, None, None], [9, None, None]], [17, [14, None, None], None]]
        test_tree1 = binary_tree(node_list1)
        test_tree2 = binary_tree(node_list2)

        self.assertFalse(test_tree1.verify_bst())
        self.assertTrue(test_tree2.verify_bst())

    def test_breadth_first_search(self):
        node_list = [5, [12, [9, None, None], [3, None, None]], [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)

        self.assertTrue(test_tree.breadth_first_search(3))
        self.assertFalse(test_tree.breadth_first_search(14))

    def test_depth_first_search(self):
        node_list = [5, [12, [9, None, None], [3, None, None]], [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)

        self.assertTrue(test_tree.depth_first_search(3))
        self.assertFalse(test_tree.depth_first_search(14))

    def test_invert(self):
        node_list = [5, [12, [9, None, None], [3, None, None]], [17, None, [2, None, None]]]
        test_tree = binary_tree(node_list)
        inverted_list = [5, [17, [2, None, None], None], [12, [3, None, None], [9, None, None]]]
        inverted_tree = binary_tree(inverted_list)

        self.assertEqual(test_tree.invert(), inverted_tree)


class test_binary_search_tree(unittest.TestCase):

    def test_min(self):
        node_list = [12, [5, [2, None, None], [9, None, None]], [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)

        self.assertEqual(test_tree.minimum(), 2)

    def test_max(self):
        node_list = [12, [5, [2, None, None], [9, None, None]], [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)

        self.assertEqual(test_tree.maximum(), 17)

    def test_search(self):
        node_list = [12, [5, [2, None, None], [9, None, None]], [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)

        self.assertTrue(test_tree.search(9))
        self.assertFalse(test_tree.search(-3))

    def test_retrieve(self):
        node_list = [12, [5, [2, None, None], [9, None, None]], [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)

        test_node = test_tree.retrieve(5)

        self.assertEqual(test_node.val, 5)
        self.assertEqual(test_node.left.val, 2)
        self.assertEqual(test_node.right.val, 9)
        self.assertEqual(test_tree.retrieve(7), None)

    def test_successor(self):
        node_list = [12, [5, [2, None, None], [9, None, None]], [17, [14, None, None], None]]
        test_tree = binary_search_tree(node_list)

        self.assertEqual(test_tree.successor(5), 9)
        self.assertEqual(test_tree.successor(9), 12)
        self.assertEqual(test_tree.successor(6), 9)
        self.assertEqual(test_tree.successor(17), None)


if __name__ == '__main__':
    unittest.main()