#!python
from queue import LinkedQueue

class BinaryTreeNode(object):

    def __init__(self, data):
        """ Initializes binary tree node with given data. """
        self.data = data
        self.left, self.right = None, None

    def __repr__(self):
        """ Returns string representation of binary tree node. """
        return "BinaryTreeNode({!r})".format(self.data)

    def is_leaf(self):
        """ Returns True if node is leaf (has no children). """
        return self.left is None and self.right is None

    def is_branch(self):
        """ Returns True if node is branch (has at least one child). """
        return any((self.left, self.right))

    def height(self):
        """ Returns height of node (number of edges on longest
        downward path from node to descendant leaf node).\n
        BEST CASE = O(1) => Tree is stump.\n
        WORST CASE = O(log(n)) => Traverses through length of tree. """
        if self.is_leaf():
            return 0

        left_height, right_height = 0, 0
        if self.left is not None:                       # Checks if left child has value
            # TODO: Try self.left.height and self.right.height
            left_height = self.left.height()        # Calculates node height
        if self.right is not None:                      # Checks if right child has value
            right_height = self.right.height()      # Calculates node height
        return max(left_height, right_height) + 1       # Returns one plus max of L/R height

class BinarySearchTree(object):

    def __init__(self, items=None):
        """ Initializes binary search tree and inserts given items. """
        self.root, self.size = None, 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """ Returns string representation of binary search tree. """
        return "BinarySearchTree({} NODES)".format(self.size)

    def is_empty(self):
        """ Returns True if binary search tree is empty (has no nodes). """
        return self.root is None

    def height(self):
        """ Returns height of tree (number of edges on longest
        downward path from tree's root node to descendant leaf node).\n
        BEST CASE = O(1) => Tree is stump.\n
        WORST CASE = O(log(n)) => Traverses through length of tree. """
        if self.root is not None:                       # Checks if root node has value
            return self.root.height()                   # Returns root node's height
        else:
            return 0

    def contains(self, item):
        """ Returns True if binary search tree contains given item.\n
        BEST CASE = O(1) => Tree is stump.\n
        WORST CASE = O(log(n)) => Traverses through length of tree. """
        node = self._find_node(item)            # Finds node with given item, if any
        return node is not None                 # Returns True if node was found, else False

    def search(self, item):
        """ Returns item in binary search tree matching given item,
        or None if given item is not found.\n
        BEST CASE = O(1) => Tree is stump.\n
        WORST CASE = O(log(n)) => Traverses through length of tree. """
        node = self._find_node(item)
        if node is not None:
            return node.data                    # Returns node's data if exists, else None
        else:
            return None

    def insert(self, item):
        """ Inserts given item in order into binary search tree.\n
        BEST CASE = O(?) => ???\n
        WORST CASE = O(?) => ??? """
        if self.is_empty():                     # Checks if tree is empty
            self.root = BinaryTreeNode(item)    # Creates new root node
            self.size += 1                      # Increments tree size
            return

        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node(item)

        if item < parent.data:                  # Checks if given item is less than parent
            parent.left = BinaryTreeNode(item)  # Creates new node as parent's left child
        elif item > parent.data:                # Checks if given item is greater than parent
            parent.right = BinaryTreeNode(item) # Creates new node as parent's right child
        self.size += 1

    '''
    def delete(self, item):
        """ Deletes given item in node in binary search tree.\n
        BEST CASE = O(1) => Tree is stump.\n
        WORST CASE = O(log(n)) => Traverses through depth of tree. """
        parent, node = self._find_parent_node(item), self._find_node(item)
        if node.is_leaf():                      # Checks if node to delete has no children
            parent = None                       # Sets parent pointer to None
            del node.data                       # Deletes node's data
        elif node.is_branch():                  # Checks if node to delete has children
            if node.left is not None:


        # 1st case: Node to be removed has no children (least complex)
        # Find item's node and parent
        # parent, node = self._find_parent_node(item), self._find_node(item)
        # Set parent pointer to null
        parent = None
        # Use <del> keyword on node's data (???)

        # 2nd case: Node to be removed has one child
        # 3rd case: Node to be removed has two children (most complex)
        return
    '''

    def _find_node(self, item):
        """ Returns node containing given item in binary search tree,
        or None if given item is not found. (Iterative)\n
        BEST CASE = O(1) => Tree is stump.\n
        WORST CASE = O(log(n)) => Traverses through depth of tree. """
        node = self.root
        while node is not None:                 # Iterates from root to closest leaf node
            if item == node.data:               # Checks if item matches node's data
                return node                     # Returns found node
            elif item < node.data:              # Checks if item is less than node's data
                node = node.left                # Descends to node's left child
            else:  # item > node.data              # Checks if item is greater than node's data
                node = node.right               # Descends to node's right child
        return None                             # Else returns None if item not found in tree

    def _find_node_recursive(self, item, node):
        """ Returns node containing given item in binary search tree,
        or None if given item is not found. (Recursive)\n
        BEST CASE = O(???)\n
        WORST CASE = O(???) """
        '''
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # TODO: Check if the given item matches the node's data
        elif ...:
            # Return the found node
            return node
        # TODO: Check if the given item is less than the node's data
        elif ...:
            # TODO: Recursively descend to the node's left child, if it exists
            return ...
        # TODO: Check if the given item is greater than the node's data
        elif ...:
            # TODO: Recursively descend to the node's right child, if it exists
            return ...
        '''

    def _find_parent_node_iterative(self, item):
        """ Returns parent node of node containing given item
        (or parent node of where given item would be if inserted)
        in tree, or None if tree is empty or has only root node. (Iterative)\n
        BEST CASE = O(1) => Tree is stump.\n
        WORST CASE = O(log(n)) => Traverses through depth of tree. """
        parent, node = None, self.root
        while node is not None:                 # Iterates from root to closest leaf node
            if item == node.data:               # Checks if item matches node's data
                return parent                   # Returns parent of found node
            elif item < node.data:              # Checks if item is less than node's data
                parent = node                   # Updates parent
                node = node.left                # Descends to node's left child
            elif item > node.data:             # Checks if item is greater than node's data
                parent = node                   # Updates parent
                node = node.right               # Descends to node's right child
        return parent                           # Else returns None if item not found in tree
        
    def _find_parent_node_recursive(self, item, node, parent=None):
        """ Returns parent node of node containing given item
        (or parent node of where given item would be if inserted)
        in tree, or None if tree is empty or has only root node. (Recursive)\n
        BEST CASE = O(???)\n
        WORST CASE = O(???) """
        # Check if starting node exists
        '''
        if node is None:
            # Not found (base case)
            return None
        # TODO: Check if the given item matches the node's data
        if ...:
            # Return the parent of the found node
            return parent
        # TODO: Check if the given item is less than the node's data
        elif ...:
            # TODO: Recursively descend to the node's left child, if it exists
            return ...  # Hint: Remember to update the parent parameter
        # TODO: Check if the given item is greater than the node's data
        elif ...:
            # TODO: Recursively descend to the node's right child, if it exists
            return ...  # Hint: Remember to update the parent parameter
        '''

    def delete(self, item):
        """ Removes given item from tree if present, or raises ValueError.\n
        BEST CASE = O(???)\n
        WORST CASE = O(???) """
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases
        # Case 1: Item-containing node is leaf (least complex)
        # Case 2: Item-containing node is parent of one child
        # Case 3: Item-containing node is parent of two children (most complex)

    def items_in_order(self):
        """ Returns in-order list of all items in binary search tree. """
        items = list()
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        return items                            # Returns in-order list of all items in tree

    def _traverse_in_order_recursive(self, node, visit):
        """ Traverses binary tree with recursive in-order traversal (DFS).
        Start at given node and visit each node with given function.\n
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node.left is not None:               # Traverses left subtree if exists
            self._traverse_in_order_recursive(node.left, visit)
        visit(node.data)                        # Visits node's data with given 'visit' function
        if node.right is not None:              # Traverses right subtree if exists
            self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = list()
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        return items                            # Returns pre-order list of all items in tree

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        visit(node.data)                        # Visits node's data with given function
        if node.left is not None:               # Traverses left subtree if exists
            self._traverse_pre_order_recursive(node.left, visit)
        if node.right is not None:              # Traverses right subtree if exists
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = list()
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        return items                            # Returns post-order list of all items in tree

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node.left is not None:               # Traverses left subtree if exists
            self._traverse_post_order_recursive(node.left, visit)
        if node.right is not None:              # Traverses right subtree if exists
            self._traverse_post_order_recursive(node.right, visit)
        visit(node.data)                        # Visit node's data with given function

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = list()
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        queue = LinkedQueue()                   # Creates queue to store nodes not yet traversed in level-order
        queue.enqueue(start_node)               # Enqueues given starting node
        while queue.is_empty() is False:        # Loops until queue is empty
            node = queue.dequeue()              # Dequeues node at front of queue
            visit(node.data)                    # Visits node's data with given function
            if node.left is not None:           # Enqueues node's left child if exists
                queue.enqueue(node.left)
            if node.right is not None:          # Enqueues node's right child if exists
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
