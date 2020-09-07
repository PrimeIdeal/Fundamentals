class node:
    """
    A simple node that contains a value and a reference to another node.
    """

    def __init__(self, val=None):
        """
        Constructor for node class.
        """
        self.val = val
        self.next = None

    def __eq__(self, other_node):
        """
        Returns True if other_node is equal to self, False otherwise.

        Define node equality as equal node values and equal values in the
        respective next nodes.
        """
        if (self.next and not other_node.next) or (not self.next and other_node.next):
            return False
        
        equal = (self.val == other_node.val)
        if equal and self.next:
            equal = equal and (self.next.val == other_node.next.val)
        
        return equal


class double_node(node):
    """
    An extension of the simple node that references a Previous node and a Next node.
    """

    def __init__(self, val=None):
        """
        Constructor for double_node class.
        """
        node.__init__(self, val)
        self.prev = None

    def __eq__(self, other_node):
        """
        Returns True if other_node is equal to self, False otherwise.

        Define double_node equality as equal double_node values and equal values in the
        respective prev and next double_nodes.
        """
        if ((self.next and not other_node.next) \
            or (not self.next and other_node.next) \
            or (self.prev and not other_node.prev) \
            or (not self.prev and other_node.prev)):
            return False
        
        equal = (self.val == other_node.val)
        if equal and self.next:
            equal = equal and (self.next.val == other_node.next.val)
        if equal and self.prev:
            equal = equal and (self.prev.val == other_node.prev.val)
        
        return equal

    def link_next(self, other_node):
        """
        Links self to its next double_node.
        """
        if other_node:
            self.next, other_node.prev = other_node, self

    def link_prev(self, other_node):
        """
        Links self to its prev double_node.
        """
        if other_node:
            self.prev, other_node.next = other_node, self

class linked_list:
    
    def __init__(self, val=None):
        """
        Constructor for linked_list class.
        """
        if val is not None:
            self.head = node(val)
        else:
            self.head = val

    def get_tail(self):
        """
        Returns the tail node of the linked_list.
        """
        tail = self.head

        if tail:
            while tail.next:
                tail = tail.next

        return tail

    def insert_head(self, new_val):
        """
        Inserts a new node at the head of the linked_list.
        """
        new_node = node(new_val)
        self.head, new_node.next = new_node, self.head

    def insert_tail(self, new_val):
        """
        Inserts a new node at the tail of the linked_list.
        """
        new_node = node(new_val)
        tail = self.get_tail()
        tail.next = new_node

    def remove_head(self):
        """
        Removes and returns the node at the head of the linked_list.
        """
        old_head = self.head
        if self.head:
            self.head = old_head.next
        old_head.next = None
        return old_head

    def remove_tail(self):
        """
        Removes and returns the node at the tail of the linked_list.
        """
        curr = self.head

        if not curr or not curr.next:
            self.head = None
            return curr

        while curr.next.next:
            curr = curr.next
        
        old_tail = curr.next
        curr.next = None

        return old_tail
    
class double_linked_list:

    def __init__(self, val=None):
        """
        Constructor for double_linked_list class.
        """
        if val is not None:
            self.head = double_node(val)
        else:
            self.head = val

    def get_tail(self):
        """
        Returns the tail double_node of the double_linked_list.
        """
        tail = self.head

        if tail:
            while tail.next:
                tail = tail.next
        
        return tail

    def insert_head(self, val):
        """
        Inserts a new double_node at the head of the double_linked_list.
        """
        new_head = double_node(val)
        old_head = self.head

        if old_head:
            old_head.link_prev(new_head)
        self.head = new_head

    def insert_tail(self, val):
        """
        Inserts a new double_node at the tail of the double_linked_list.
        """
        new_node = double_node(val)
        tail = self.get_tail()

        if not tail:
            self.head = new_node
        else:
            tail.link_next(new_node)

    def remove_head(self):
        """
        Removes and returns the double_node at the head of the double_linked_list.
        """
        old_head = self.head

        if not old_head or not old_head.next:
            self.head = None
        else:
            old_head.next.prev = None
            self.head = old_head.next
            old_head.next = None

        return old_head

    def remove_tail(self):
        """
        Removes and returns the double_node at the tail of the double_linked_list.
        """
        curr = self.head

        if not curr or not curr.next:
            self.head = None
            return curr

        while curr.next.next:
            curr = curr.next

        old_tail = curr.next
        curr.next, old_tail.prev = None, None
        return old_tail
