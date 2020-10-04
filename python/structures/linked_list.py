from __future__ import annotations

from typing import (
    Any,
    List
)


class linked_list:
    """
    A simple linked list where each node contains a value and a
    reference to the next node in the list.
    """

    def __init__(self, node_list=None):
        """
        Constructor for the linked_list class.
        """
        self.empty = False if node_list else True
        self.val = node_list[0] if node_list else None
        self.next = linked_list(node_list=node_list[1:]) \
            if node_list and node_list[1:] else None

    def __str__(self):
        """
        Returns the linked list's unique string representation.
        """
        return '['+'->'.join(str(elt) for elt in self.serialize())+']'

    def __eq__(self, other_list):
        """
        Returns True if other_list is equal to self, False otherwise.
        """
        curr1, curr2 = self, other_list
        while curr1 and curr2:
            if curr1.empty != curr2.empty or curr1.val != curr2.val:
                return False
            curr1, curr2 = curr1.next, curr2.next

        return not (curr1 or curr2)

    def serialize(self):
        """
        Returns the linked list's unique array representation.
        """
        curr = self
        list_representation = []

        while curr:
            if not curr.empty:
                list_representation.append(curr.val)
            curr = curr.next

        return list_representation

    def get_node(self, val):
        """
        Returns the first node containing a given value if it exists
        in the list, None otherwise.
        """
        curr = self

        while curr:
            if curr.val == val:
                return curr
            curr = curr.next

        return None

    def get_tail(self):
        """
        Returns the tail node of the linked list.
        """
        curr = self

        while curr and curr.next:
            curr = curr.next

        return curr

    def insert_head(self, val):
        """
        Returns a new linked list with a node containing the given value at
        its head.
        """
        if self.empty:
            self.val, self.empty = val, False
            return self
        else:
            new_list = linked_list(node_list=[val])
            new_list.next = self
            return new_list

    def insert_tail(self, val):
        """
        Appends a new node containing the given value at the tail of the
        linked list.
        """
        if self.empty:
            self.val, self.empty = val, False
        else:
            tail = self.get_tail()
            tail.next = linked_list(node_list=[val])

    def remove_head(self):
        """
        Removes the head node of the linked list.
        """
        if not self.empty:
            if not self.next:
                self.val, self.empty = None, True
            else:
                self.val, self.next = self.next.val, self.next.next

    def remove_tail(self):
        """
        Removes the tail node of the linked list.
        """
        if not self.empty:
            curr = self
            if not curr.next:
                self.val, self.empty = None, True
            else:
                while curr.next and curr.next.next:
                    curr = curr.next
                curr.next = None

    def delete_node(self, val):
        """
        Removes the first node containing the given value.
        """
        if self.val == val:
            if not self.next:
                self.val, self.empty = None, True
            else:
                self.val, self.next = self.next.val, self.next.next

        curr = self

        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
                break
            curr = curr.next

    def reverse(self, recursive=True):
        """
        Reverses the linked list.
        """
        curr = self

        if recursive:
            if curr and curr.next:
                temp = curr.next.reverse()
                curr.next.next = curr
                curr.next = None
                curr = temp
        else:
            prev = None
            while curr:
                curr.next, curr, prev = prev, curr.next, curr
            curr = prev

        return curr


class double_linked_list:
    """
    A doubly linked list where each node contains a value and references to its
    respective previous and next nodes in the list.
    """

    def __init__(
        self,
        node_list: List[Any] = None,
        prev: double_linked_list = None
    ):
        """
        Constructor for the double_linked_list class.

        Parameters
        ----------
        node_list : List[Any]
            Optional: Ordered list of values to be inserted into the doubly
            linked list.
        prev: double_linked_list
            Optional: The previous node in the doubly linked list.
        """
        self.empty = False if node_list else True
        self.val = node_list[0] if node_list else None
        self.prev = prev
        self.next = double_linked_list(node_list=node_list[1:], prev=self) \
            if node_list and node_list[1:] else None

    def __str__(self) -> str:
        """
        Returns the doubly linked list's unique string representation.

        Returns
        -------
        str
            String representation of the double_linked_list object.
        """
        return '['+'<->'.join(str(elt) for elt in self.serialize())+']'

    def __eq__(self, other_list: double_linked_list) -> bool:
        """
        Determines equality between double_linked_list objects.

        Parameters
        ----------
        other_list : double_linked_list
            Doubly linked list to compare self with.

        Returns
        -------
        bool
            True if self is equal to other_list, False otherwise.
        """
        if not isinstance(other_list, double_linked_list):
            return False

        curr1, curr2 = self, other_list
        while curr1 and curr2:
            if curr1.empty != curr2.empty or curr1.val != curr2.val:
                return False
            curr1, curr2 = curr1.next, curr2.next

        return not (curr1 or curr2)

    def serialize(self) -> List[Any]:
        """
        Returns the doubly linked list's unique array representation.

        Returns
        -------
        List[Any]
            Array representation of the double_linked_list object.
        """
        curr = self
        list_representation = []

        while curr:
            if not curr.empty:
                list_representation.append(curr.val)
            curr = curr.next

        return list_representation

    def get_tail(self):
        pass

    def insert_head(self, val):
        pass

    def insert_tail(self, val):
        pass

    def remove_head(self, val):
        pass

    def remove_tail(self, val):
        pass
