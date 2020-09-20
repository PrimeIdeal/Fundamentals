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
            if node_list[1:] else None

    def __str__(self):
        """
        Returns the linked list's unique string representation.
        """
        str_representation = '['

        str_representation += '->'.join(str(elt) for elt in self.serialize())

        return str_representation + ']'

    def __eq__(self, other_list):
        """
        Returns True if other_list is equal to self, False otherwise.
        """
        return self.serialize() == other_list.serialize()

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
        pass

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
