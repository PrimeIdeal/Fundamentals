import unittest

from structures.linked_list import node, double_node


class test_nodes(unittest.TestCase):

    def test_equal(self):
        a, b = node(3), node(3)
        c, d = node(4), node(4)

        a.next, b.next = c, d

        self.assertEqual(c, d)
        self.assertEqual(a, b)

    def test_not_equal(self):
        a, b, c = node(3), node(4), node(3)
        c.next = b

        self.assertNotEqual(a, b)
        self.assertNotEqual(a, c)


class test_double_nodes(unittest.TestCase):

    def test_equal(self):
        a, b = double_node(3), double_node(3)
        c, d = double_node(4), double_node(4)
        e, f = double_node(5), double_node(5)
        g, h = double_node(6), double_node(6)

        a.link_next(c)
        a.link_prev(e)
        b.link_next(d)
        b.link_prev(f)

        self.assertEqual(a, b)
        self.assertEqual(c, d)
        self.assertEqual(e, f)
        self.assertEqual(g, h)

    def test_not_equal(self):
        a, b, c = double_node(3), double_node(4), double_node(3)
        d, e, f = double_node(5), double_node(6), double_node(5)

        self.assertNotEqual(a, b)
        c.link_next(b)
        self.assertNotEqual(a, c)
        f.link_prev(e)
        self.assertNotEqual(d, f)

    def test_link_next(self):
        a, b = double_node(7), double_node(8)
        a.link_next(b)
        d, e = double_node(9), None
        d.link_next(e)

        self.assertEqual(a.next, b)
        self.assertEqual(b.prev, a)
        self.assertEqual(d.next, None)

    def test_link_prev(self):
        a, b = double_node(7), double_node(8)
        a.link_prev(b)
        d, e = double_node(9), None
        d.link_prev(e)

        self.assertEqual(a.prev, b)
        self.assertEqual(b.next, a)
        self.assertEqual(d.prev, None)


if __name__ == '__main__':
    unittest.main()
