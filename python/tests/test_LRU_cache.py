import pytest

from python.structures.LRU_cache import LRU_cache


class TestLRUCache:

    def test_update(self):
        cache = LRU_cache()
        cache.update(2)

        assert cache.get_kth_element() == 2

        cache.update(7)

        assert cache.get_kth_element() == 7

        cache.update(2)

        assert cache.get_kth_element() == 2

    def test_get_kth_element(self):
        cache = LRU_cache()
        cache.update(2)
        cache.update(7)
        cache.update(8)
        cache.update(7)

        assert cache.get_kth_element() == 7
        assert cache.get_kth_element(2) == 8
        assert cache.get_kth_element(3) == 2
        assert cache.get_kth_element(4) is None
