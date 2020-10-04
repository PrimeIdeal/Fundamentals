import pytest

from python.structures.LRU_cache import LRU_cache


class TestLRUCache:
    """
    Test class for the LRU_cache class.
    """

    @pytest.fixture(scope='class')
    def update_cache(self):
        cache = LRU_cache()

        yield cache

    @pytest.mark.parametrize(
        'elt',
        [2, 7, 2]
    )
    def test_update(self, update_cache, elt):
        update_cache.update(elt)

        assert update_cache.get_kth_element() == elt

    @pytest.fixture(scope='class')
    def kth_elt_cache(self):
        cache = LRU_cache()
        for elt in [2, 7, 8, 7]:
            cache.update(elt)

        yield cache

    @pytest.mark.parametrize(
        'k, expected',
        [
            (1, 7),
            (2, 8),
            (3, 2),
            (4, None)
        ]
    )
    def test_get_kth_element(self, kth_elt_cache, k, expected):

        if expected is not None:
            assert kth_elt_cache.get_kth_element(k=k) == expected
        else:
            assert kth_elt_cache.get_kth_element(k=k) is None
