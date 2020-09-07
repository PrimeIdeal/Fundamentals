import unittest

from structures.LRU_cache import LRU_cache


class test_LRU_cache(unittest.TestCase):

    def test_update(self):
        cache = LRU_cache()
        cache.update(2)

        self.assertEqual(cache.get_kth_element(), 2)

        cache.update(7)

        self.assertEqual(cache.get_kth_element(), 7)

        cache.update(2)

        self.assertEqual(cache.get_kth_element(), 2)

    def test_get_kth_element(self):
        cache = LRU_cache()
        cache.update(2)
        cache.update(7)
        cache.update(8)
        cache.update(7)

        self.assertEqual(cache.get_kth_element(), 7)
        self.assertEqual(cache.get_kth_element(2), 8)
        self.assertEqual(cache.get_kth_element(3), 2)
        self.assertEqual(cache.get_kth_element(4), None)


if __name__ == '__main__':
    unittest.main()