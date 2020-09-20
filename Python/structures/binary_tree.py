from collections import deque


def _is_sorted(input_list, ascending=True):
    """
    Helper function. Returns True if a list of numbers is sorted, False
    otherwise. List must be nonempty.
    """
    curr = input_list[0]

    for num in input_list[1:]:
        if (ascending and num < curr) or (not ascending and num > curr):
            return False
        curr = num

    return True


class binary_tree:
    """
    An acyclic graph where all nodes contain values and have at most 3
    neighbors.
    """

    def __init__(self, node_list=None):
        """
        Constructor for binary_tree class.

        Recursively constructs a binary tree from a nested list of node values.
        If a node is missing a child node, its corresponding list element must
        be None, ie.

            3
           /
          2

        should be represented as [3, [2, None, None], None].
        """
        self.val = node_list[0] if node_list else None
        self.left = binary_tree(node_list[1]) \
            if node_list and node_list[1] else None
        self.right = binary_tree(node_list[2]) \
            if node_list and node_list[2] else None

    def __str__(self):
        """
        Returns the unique string representation of the binary tree.
        """
        node_str = f'[{self.val}'
        if self.left:
            node_str += ',' + str(self.left)
        else:
            node_str += ',None'
        if self.right:
            node_str += ',' + str(self.right)
        else:
            node_str += ',None'
        node_str += ']'

        return node_str

    def __eq__(self, other_tree):
        """
        Returns True if other_tree is equal to self, False otherwise.
        """
        return self.serialize() == other_tree.serialize()

    def serialize(self):
        """
        Converts the binary tree to its unique representation as a nested list
        of node values.
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
        Returns True if the binary tree obeys the binary search tree property,
        False otherwise.
        """
        return _is_sorted(self.inorder_traversal())

    def breadth_first_search(self, val, retrieve=False):
        """
        Returns True if a given value exists in the binary tree, False
        otherwise. If retrieval is specified, returns the node containing
        the value.

        Implementation of the breadth-first search algorithm.
        """
        node_q = deque()
        node_q.append(self)

        while len(node_q) > 0:
            curr = node_q.popleft()
            if curr.val == val:
                if retrieve:
                    return curr
                return True
            if curr.left:
                node_q.append(curr.left)
            if curr.right:
                node_q.append(curr.right)

        if retrieve:
            return None
        return False

    def depth_first_search(self, val, retrieve=False):
        """
        Returns True if a given value exists in the binary tree, False
        otherwise. If retrieval is specified, returns the node containing
        the value.

        Implementation of the depth-first search algorithm.
        """
        node_stack = []
        node_stack.append(self)

        while node_stack:
            curr = node_stack.pop()
            if curr.val == val:
                if retrieve:
                    return curr
                return True
            if curr.right:
                node_stack.append(curr.right)
            if curr.left:
                node_stack.append(curr.left)

        if retrieve:
            return None
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
    """
    A binary tree that obeys the binary search tree property: for any node N,
    x <= N.val for all node values x in N.left and y > N.val for all node
    values y in N.right.
    """

    def __init__(self, node_list=None, parent=None):
        """
        Constructor for binary_search_tree class.

        Recursively constructs a binary tree from a nested list of node values.
        If a node is missing a child node, its corresponding list element must
        be None, ie.

            3
           /
          2

        should be represented as [3, [2, None, None], None].

        The nested list must obey the binary search tree property.
        """
        self.parent = parent
        self.val = node_list[0] if node_list else None
        self.left = binary_search_tree(
            node_list[1], parent=self
        ) if node_list and node_list[1] else None
        self.right = binary_search_tree(
            node_list[2], parent=self
        ) if node_list and node_list[2] else None

    def minimum(self, retrieve=False):
        """
        Returns the minimum value in the binary search tree. If retrieval is
        specified, returns the node containing the minimum value instead.
        """
        curr = self
        while curr.left:
            curr = curr.left

        if retrieve:
            return curr
        else:
            return curr.val

    def maximum(self, retrieve=False):
        """
        Returns the maximum value in the binary search tree. If retrieval is
        specified, returns the node containing the maximum value instead.
        """
        curr = self
        while curr.right:
            curr = curr.right

        if retrieve:
            return curr
        else:
            return curr.val

    def search(self, val, retrieve=False):
        """
        Returns True if a given value exists in the binary search tree, False
        otherwise. If retrieval is specified, returns the node containing the
        given value instead.
        """
        curr = self
        while curr and curr.val:
            if curr.val == val:
                if retrieve:
                    return curr
                else:
                    return True
            if curr.val < val:
                curr = curr.right
            else:
                curr = curr.left

        if retrieve:
            return None
        else:
            return False

    def successor(self, val=None, retrieve=False):
        """
        Returns the smallest value greater than a given node value. If the
        value is not specified, returns the smallest value greater than the
        current node's value. If retrieval is specified, returns the node
        with the smallest value greater than the given value.
        """
        curr = self.search(val, retrieve=True) if val else self
        if curr.right:
            return curr.right.minimum(retrieve=retrieve)
        curr_parent = curr.parent
        while curr_parent and curr is curr_parent.right:
            curr = curr_parent
            curr_parent = curr_parent.parent

        if curr_parent and not retrieve:
            return curr_parent.val
        return curr_parent

    def predecessor(self, val=None, retrieve=False):
        """
        Returns the greatest value smaller than a given node value. If the
        value is not specified, returns the greatest value smaller than the
        current node's value. If retrieval is specified, returns the node
        with the greatest value smaller than the given value.
        """
        curr = self.search(val, retrieve=True) if val else self
        if curr.left:
            return curr.left.maximum(retrieve=retrieve)
        curr_parent = curr.parent
        while curr_parent and curr is curr_parent.left:
            curr = curr_parent
            curr_parent = curr_parent.parent

        if curr_parent and not retrieve:
            return curr_parent.val
        return curr_parent

    def insert(self, val):
        """
        Inserts a new node with the given value into the binary tree. Assumes
        all nodes have distinct values.
        """
        curr_parent, curr = None, self

        while curr and curr.val:
            curr_parent = curr
            if curr.val == val:
                return
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right

        new_node = binary_search_tree(
            node_list=[val, None, None], parent=curr_parent
        )

        if not curr_parent:
            self.val = val
            self.parent = None
            self.left = None
            self.right = None
        elif val < curr_parent.val:
            curr_parent.left = new_node
        else:
            curr_parent.right = new_node

    def transplant(self, node_to_replace, replacement_node):
        """
        Replaces one tree as a child of its parent with another tree.
        """
        if not node_to_replace.parent:
            node_to_replace.val = replacement_node.val
            node_to_replace.left = replacement_node.left
            node_to_replace.right = replacement_node.right
        elif node_to_replace is node_to_replace.parent.left:
            node_to_replace.parent.left = replacement_node
        else:
            node_to_replace.parent.right = replacement_node
        if replacement_node:
            replacement_node.parent = node_to_replace.parent

    def delete(self, val):
        """
        Removes the node containing a given value from the binary tree.
        """
        to_delete = self.search(val, retrieve=True)

        if not to_delete.left:
            self.transplant(to_delete, to_delete.right)
        elif not to_delete.right:
            self.transplant(to_delete, to_delete.left)
        else:
            min_node = to_delete.right.minimum(retrieve=True)
            if min_node.parent is not to_delete:
                self.transplant(min_node, min_node.right)
                min_node.right = to_delete.right
                min_node.right.parent = min_node
            self.transplant(to_delete, min_node)
            min_node.left = to_delete.left
            min_node.left.parent = min_node

    def distance(self, val1, val2):
        """
        Determines the distance between the node containing val1 and
        the node containing val2.
        """
        dist = 0
        max_val, min_val = max(val1, val2), min(val1, val2)
        curr1, curr2 = self, self

        try:
            while curr1.val != min_val and curr2.val != max_val:
                curr1 = curr1.right if curr1.val < min_val else curr1.left
                curr2 = curr2.right if curr2.val < max_val else curr2.left
                if curr1 is not curr2:
                    dist += 2

            if not (curr1.val == min_val and curr2.val == max_val):
                curr, last_val = (curr1, min_val) if curr1.val != min_val \
                    else (curr2, max_val)
                while curr.val != last_val:
                    curr = curr.right if curr.val < last_val else curr.left
                    dist += 1

            return dist

        except AttributeError:
            if not curr1 and not curr2:
                raise ValueError(
                    f'{val1} and {val2} do not exist in the tree.'
                )
            else:
                bad_val = min_val if not curr1 else max_val
                raise ValueError(f'{bad_val} does not exist in the tree.')
