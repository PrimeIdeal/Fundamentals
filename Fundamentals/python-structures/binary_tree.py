from collections import deque


class binary_tree:
    """
    An acyclic graph where all nodes contain values and have at most 3 neighbors.
    """

    def __init__(self, node_list=None):
        """
        Constructor for binary_tree class.

        Recursively constructs a binary tree from a nested list of node values. If a node is
        missing a child node, its corresponding list element must be None, ie.

            3
           /
          2
        
        should be represented as [3, [2, None, None], None].
        """
        self.val = node_list[0] if node_list else None
        self.left = binary_tree(node_list[1]) if node_list and node_list[1] else None
        self.right = binary_tree(node_list[2]) if node_list and node_list[2] else None

    def __str__(self):
        """
        Returns the unique string representation of the binary tree.
        """
        node_str = f'[{self.val}'
        if self.left:
            node_str += ', ' + str(self.left)
        else:
            node_str += ', None'
        if self.right:
            node_str += ', ' + str(self.right)
        else:
            node_str += ', None'
        node_str += ']'
        
        return node_str

    def __eq__(self, other_tree):
        """
        Returns True if other_tree is equal to self, False otherwise.
        """
        return self.serialize() == other_tree.serialize()

    def serialize(self):
        """
        Converts the binary tree to its unique representation as a nested list of node values.
        """
        node_list = [self.val, None, None]
        if self.left:
            node_list[1] = self.left.serialize()
        if self.right:
            node_list[2] = self.right.serialize()

        return node_list

    def preorder_traversal(self):
        """
        Returns the preorder traversal of the binary tree.
        """
        traversal = [self.val]
        if self.left:
            traversal += self.left.preorder_traversal()
        if self.right:
            traversal += self.right.preorder_traversal()

        return traversal


    def inorder_traversal(self):
        """
        Returns the inorder traversal of the binary tree.
        """
        traversal = []
        if self.left:
            traversal += self.left.inorder_traversal()
        traversal.append(self.val)
        if self.right:
            traversal += self.right.inorder_traversal()
        
        return traversal

    def postorder_traversal(self):
        """
        Returns the postorder traversal of the binary tree.
        """
        traversal = []
        if self.left:
            traversal += self.left.postorder_traversal()
        if self.right:
            traversal += self.right.postorder_traversal()
        traversal.append(self.val)

        return traversal

    def verify_bst(self):
        """
        Returns True if the binary tree obeys the binary search tree property, False otherwise.
        """
        inorder_traversal = self.inorder_traversal()

        return inorder_traversal == sorted(inorder_traversal)

    def breadth_first_search(self, val):
        """
        Returns True if a given value exists in the binary tree, False otherwise.

        Implementation of the breadth-first search algorithm.
        """
        node_q = deque()
        node_q.append(self)

        while len(node_q) > 0:
            curr = node_q.popleft()
            if curr.val == val:
                return True
            if curr.left:
                node_q.append(curr.left)
            if curr.right:
                node_q.append(curr.right)
            
        return False

    def depth_first_search(self, val):
        """
        Returns True if a given value exists in the binary tree, False otherwise.

        Implementation of the depth-first search algorithm.
        """
        node_stack = []
        node_stack.append(self)

        while node_stack:
            curr = node_stack.pop()
            if curr.val == val:
                return True
            if curr.right:
                node_stack.append(curr.right)
            if curr.left:
                node_stack.append(curr.left)

        return False

    def invert(self):
        """
        Inverts the binary tree.
        """
        new_tree = binary_tree()
        new_tree.val = self.val
        if self.left:
            new_tree.right = self.left.invert()
        if self.right:
            new_tree.left = self.right.invert()

        return new_tree


class binary_search_tree(binary_tree):

    def __init__(self):
        pass

    def minimum(self):
        pass

    def maximum(self):
        pass

    def search(self):
        pass

    def retrieve(self):
        pass

    def successor(self):
        pass

    def predecessor(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass
