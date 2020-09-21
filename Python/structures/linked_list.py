class linked_list:
    """
    A simple linked list where each node contains a value and a
    reference to the next node in the list.
    """

    def __init__(self, node_list=None):
        """
        Constructor for the linked_list class.
        """
        self.val = node_list[0] if node_list else None
        self.next = linked_list(node_list=node_list[1:]) \
            if node_list and node_list[1:] else None

    def __str__(self):
        """
        Returns the linked list's unique string representation.
        """
        return '->'.join(str(elt) for elt in self.serialize())

    def __eq__(self, other_list):
        """
        Returns True if other_list is equal to self, False otherwise.
        """
        curr1, curr2 = self, other_list
        while curr1 and curr2:
            if curr1.val != curr2.val:
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
        pass

    def insert_head(self):
        pass

    def insert_tail(self):
        pass

    def remove_head(self):
        pass

    def remove_tail(self):
        pass

    def delete_node(self, val):
        pass
