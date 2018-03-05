#!python

from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        return self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        if self.is_empty():
            return None
        return self.list.get_at_index(0)

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        if self.is_empty():
            raise ValueError("\n\nSTACK IS EMPTY.\n")
        else:
            top_stack_item = self.peek()
            self.list.delete(top_stack_item)
            return top_stack_item


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """ Initializes stack and pushes given items, if any. """
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """ Returns string representation of stack. """
        return "\nStack({} items, top={})".format(self.length(), self.peek())

    def is_empty(self):
        """ Returns True if stack is empty, or False otherwise. """
        if len(self.list) == 0:
            return True
        return False

    def length(self):
        """ Returns number of items in stack. """
        return len(self.list)

    def push(self, item):
        """ Inserts given item on top of stack.\n
        BEST CASE: O(???) –-> \n
        WORST CASE: O(???) --> """
        self.list.append(item)

    def peek(self):
        """ Returns item on top of stack without removing it,
        or None if stack is empty."""
        if self.is_empty():
            return None
        return self.list[len(self.list) - 1]

    def pop(self):
        """ Removes and returns item on top of stack,
        or raises ValueError if stack is empty.\n
        BEST CASE = O(???) --> \n
        WORST CASE = O(???) -->  """
        if self.is_empty():
            raise ValueError("\n\nSTACK IS EMPTY.\n")
        return self.list.pop()


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
