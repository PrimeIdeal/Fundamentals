from typing import Hashable

from python.structures.linked_list import double_linked_list


class LRU_cache:
    """
    Given a set of elements S = (a, b, c, ...) and some operation f that acts
    on S over time, the LRU cache maintains an up to date record of the order
    in which f acted on the elements of S and can retrieve the least recently
    used element in O(1) time.
    """

    def __init__(self):
        """
        Constructor for LRU_cache class.
        """
        self.elements = double_linked_list()
        self.node_map = {}

    def update(self, element: Hashable):
        """
        Updates the least recently used element in the cache.

        Parameters
        ----------
        element : Hashable
            Element to be updated.
        """
        if element in self.node_map:
            old_node = self.node_map[element]
            old_node.prev.link_next(old_node.next)
        self.elements.insert_head(element)
        self.node_map[element] = self.elements.head

    def get_kth_element(self, k: int = 1) -> Hashable:
        """
        Returns the kth least recently used element in the cache.

        Parameters
        ----------
        k : int
            Element to be retrieved (1st by default, elements are 1-indexed).

        Returns
        -------
        Hashable
            The kth least recently used element.
        """
        curr = self.elements.head

        if not curr:
            return curr

        while curr.next and k > 1:
            curr = curr.next
            k -= 1
        if k > 1:
            return None
        return curr.val
