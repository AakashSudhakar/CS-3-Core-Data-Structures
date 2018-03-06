#!python

from linkedlist import LinkedList


""" Implement LinkedQueue below, then change the assignment at the bottom
to use this Queue implementation to verify it passes all tests """

class LinkedQueue(object):

    def __init__(self, iterable=None):
        """ Initializes queue and enqueues given items, if any. """
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """ Returns string representation of queue. """
        return "Queue({} items, front={})".format(self.length(), self.front())

    def is_empty(self):
        """ Returns True if queue is empty, or False otherwise. """
        return self.list.is_empty()

    def length(self):
        """ Returns number of items in queue. """
        return self.list.size

    def enqueue(self, item):
        """ Inserts given item at back of queue.\n
        BEST/WORST CASE: O(1) --> Appends item at front of queue. """
        return self.list.append(item)

    def front(self):
        """ Returns item at front of queue without removing it,
        or None if queue is empty. """
        if self.is_empty():
            return None
        return self.list.get_at_index(0)

    def dequeue(self):
        """ Removes and returns item at front of queue,
        or raises ValueError if queue is empty.\n
        BEST/WORST CASE: O(1) --> Deletes item at front of queue. """
        if self.is_empty():
            raise ValueError("\n\nQUEUE IS EMPTY.\n")
        else:
            front_queue_item = self.front()
            self.list.delete(front_queue_item)
            return front_queue_item


""" Implement ArrayQueue below, then change the assignment at the bottom
to use this Queue implementation to verify it passes all tests """
class ArrayQueue(object):

    def __init__(self, iterable=None):
        """ Initializes queue and enqueues given items, if any. """
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def __repr__(self):
        """ Returns string representation of queue. """
        return "Queue({} items, front={})".format(self.length(), self.front())

    def is_empty(self):
        """ Returns True if queue is empty, or False otherwise. """
        if len(self.list) == 0:
            return True
        return False

    def length(self):
        """ Returns number of items in queue. """
        return len(self.list)

    def enqueue(self, item):
        """ Inserts given item at back of queue.\n
        BEST/WORST CASE: O(1) --> Appends item at back of queue. """
        return self.list.append(item)

    def front(self):
        """ Returns item at front of queue without removing it,
        or None if queue is empty. """
        if self.is_empty():
            return None
        return self.list[0]

    def dequeue(self):
        """ Removes and returns item at front of queue,
        or raises ValueError if queue is empty.\n
        BEST/WORST CASE: O(1) --> Removes item at front of queue. """
        if self.is_empty():
            raise ValueError("\n\nQUEUE IS EMPTY.\n")
        return self.list.pop(0)


""" Implement LinkedQueue and ArrayQueue above, then change the assignment below
to use each of your Queue implementations to verify they each pass all tests """
# Queue = LinkedQueue
Queue = ArrayQueue
