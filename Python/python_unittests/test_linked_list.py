import unittest

from structures.linked_list import (
    double_linked_list,
    double_node,
    linked_list,
    node
)


class test_linked_list(unittest.TestCase):

    def test_get_tail(self):
        l = linked_list(7)
        l.insert_head(8)
        m = linked_list(19)
        n = linked_list(27)
        n.remove_tail()

        self.assertEqual(l.get_tail(), node(7))
        self.assertEqual(m.get_tail(), node(19))
        self.assertEqual(n.get_tail(), None)

    def test_insert_head(self):
        a, b = node(7), node(8)
        b.next = a
        l = linked_list(7)

        self.assertEqual(l.head, a)

        l.insert_head(8)

        self.assertEqual(l.head, b)

    def test_insert_tail(self):
        l = linked_list(7)
        l.insert_tail(8)
        l.insert_tail(9)
        
        self.assertEqual(l.get_tail(), node(9))

    def test_remove_head(self):
        l = linked_list(7)
        l.insert_tail(8)

        self.assertEqual(l.remove_head(), node(7))
        self.assertEqual(l.head, node(8))

    def test_remove_tail(self):
        l = linked_list(7)
        l.insert_head(8)

        self.assertEqual(l.remove_tail(), node(7))
        self.assertEqual(l.get_tail(), node(8))


class test_double_linked_list(unittest.TestCase):

    def test_get_tail(self):
        l = double_linked_list(7)
        l.insert_head(8)
        a, b = double_node(7), double_node(8)
        a.link_prev(b)
        m = double_linked_list(19)
        n = double_linked_list(27)
        n.remove_head()

        self.assertEqual(l.get_tail(), a)
        self.assertEqual(m.get_tail(), double_node(19))
        self.assertEqual(n.get_tail(), None)

    def test_insert_head(self):
        l = double_linked_list(7)
        l.insert_head(8)
        a, b = double_node(7), double_node(8)
        b.link_next(a)

        self.assertEqual(l.head, b)

    def test_insert_tail(self):
        l = double_linked_list(7)
        l.insert_tail(8)
        a, b = double_node(7), double_node(8)
        b.link_prev(a)

        self.assertEqual(l.get_tail(), b)

    def test_remove_head(self):
        l = double_linked_list(7)
        l.insert_tail(8)

        self.assertEqual(l.remove_head(), double_node(7))
        self.assertEqual(l.head, double_node(8))
    
    def test_remove_tail(self):
        l = double_linked_list(7)
        l.insert_head(8)

        self.assertEqual(l.remove_tail(), double_node(7))
        self.assertEqual(l.get_tail(), double_node(8))


if __name__ == '__main__':
    unittest.main()
