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

    def __init__(self, node_list: List[Any] = None):
        """
        Constructor for the linked_list class.

        Parameters
        ----------
        node_list : List[Any]
            Optional: Ordered list of values to be inserted into the doubly
            linked list.
        """
        self.empty = False if node_list else True
        self.val = node_list[0] if node_list else None
        self.next = linked_list(node_list=node_list[1:]) \
            if node_list and node_list[1:] else None

    def __str__(self) -> str:
        """
        Returns the linked list's unique string representation.

        Returns
        -------
        str
            String representation of the linked_list object.
        """
        return '['+'->'.join(str(elt) for elt in self.serialize())+']'

    def __eq__(self, other_list: linked_list) -> bool:
        """
        Determines if self is equal to other_list.

        Parameters
        ----------
        other_list : linked_list
            Linked list to compare self to.

        Returns
        -------
        bool
            True if other_list is equal to self, False otherwise.
        """
        if not isinstance(other_list, linked_list):
            return False

        curr1, curr2 = self, other_list
        while curr1 and curr2:
            if curr1.empty != curr2.empty or curr1.val != curr2.val:
                return False
            curr1, curr2 = curr1.next, curr2.next

        return not (curr1 or curr2)

    def serialize(self) -> List[Any]:
        """
        Returns the linked list's unique array representation.

        Returns
        -------
        List[Any]
            Array representation of the linked_list object.
        """
        curr = self
        list_representation = []

        while curr:
            if not curr.empty:
                list_representation.append(curr.val)
            curr = curr.next

        return list_representation

    def get_node(self, val: Any) -> linked_list:
        """
        Returns the first node containing a given value if it exists
        in the list, None otherwise.

        Parameters
        ----------
        val : Any
            Node value to search for.

        Returns
        -------
        linked_list
            The node containing the value.
        """
        curr = self

        while curr:
            if curr.val == val:
                return curr
            curr = curr.next

        return None

    def get_tail(self) -> linked_list:
        """
        Returns the tail node of the linked list.

        Returns
        -------
        linked_list
            The final node of the linked_list object.
        """
        curr = self

        while curr and curr.next:
            curr = curr.next

        return curr

    def insert_head(self, val: Any) -> linked_list:
        """
        Returns a new linked list with a node containing the given value at
        its head.

        Parameters
        ----------
        val : Any
            Node value to be inserted.

        Returns
        -------
        linked_list
            The list with the new node at its head.
        """
        if self.empty:
            self.val, self.empty = val, False
            return self
        else:
            new_list = linked_list(node_list=[val])
            new_list.next = self
            return new_list

    def insert_tail(self, val: Any):
        """
        Appends a new node containing the given value at the tail of the
        linked list.

        Parameters
        ----------
        val : Any
            Node value to be inserted.
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

    def delete_node(self, val: Any):
        """
        Removes the first node containing the given value.

        Parameters
        ----------
        val : Any
            Value to search for.
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

    def reverse(self, recursive=True) -> linked_list:
        """
        Reverses the linked list.

        Parameters
        ----------
        recursive : bool
            Optional: Indicates whether to use recursive or iterative
            implementation (recursive by default).

        Returns
        -------
        linked_list
            The list in reverse order.
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


class double_linked_list(linked_list):
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

    def insert_head(self, val: Any) -> double_linked_list:
        """
        Inserts a new node containing the given value at the head of the
        doubly linked list and returns the new list.

        Parameters
        ----------
        val : Any
            Value to be inserted.

        Returns
        -------
        double_linked_list
            The list with the new node at its head.
        """
        if self.empty:
            self.val, self.empty = val, False
            return self

        new_node = double_linked_list([val])
        new_node.next, self.prev = self, new_node

        return new_node

    def insert_tail(self, val: Any):
        """
        Inserts a new node containing the given value at the tail of the
        doubly linked list.

        Parameters
        ----------
        val : Any
            Value to be inserted.
        """
        if self.empty:
            self.val, self.empty = val, False
        else:
            new_node = double_linked_list([val])
            tail = self.get_tail()
            tail.next, new_node.prev = new_node, tail

    def delete_node(self, val: Any):
        """
        Deletes the first node in the doubly linked list containing the given
        value.

        Parameters
        ----------
        val : Any
            The value to search for.
        """
        if self.val == val:
            self.remove_head()
        else:
            to_delete = self.get_node(val=val)
            if to_delete:
                if to_delete.prev:
                    to_delete.prev.next = to_delete.next
                    to_delete.prev = None
                if to_delete.next:
                    to_delete.next.prev = to_delete.prev
                    to_delete.next = None
