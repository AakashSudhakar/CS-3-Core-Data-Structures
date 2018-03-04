#!python

class Node(object):

    def __init__(self, data):
        """ Initializes node with given data. """
        self.data, self.next = data, None

    def __repr__(self):
        """ Returns string representation of node. """
        return "Node({!r})".format(self.data)


class LinkedList(object):

    def __init__(self, iterable=None):
        """ Initializes linked list and appends given items, if any. """
        self.head = None                            # First node
        self.tail = None                            # Last node
        self.size = 0                               # Number of nodes

        # Append the given items
        if iterable:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """ Returns formatted string representation of linked list. """
        items = ["({!r})".format(item) for item in self.items()]
        return "[{}]".format(" --> ".join(items))

    def __repr__(self):
        """ Returns string representation of linked list. """
        return "LinkedList({!r})".format(self.items())

    def items(self):
        """ Returns list of all items in linked list.\n
        BEST/WORST CASE = O(n) --> Must loop through all data. """
        result, node = list(), self.head            # Create new list and node instance (constant time)

        # Loop until the node is None, which is one node too far past the tail
        while node:                                 # n iterations because no early exit
            result.append(node.data)                # Append node's data to results (constant time)
            node = node.next                        # Skip to next node (constant time)
        return result  

    def is_empty(self):
        """ Returns True if linked list is empty, or False. """
        return self.head is None

    def length(self):
        """ Returns length of linked list by traversing nodes.\n
        BEST/WORST CASE = O(n) --> Must iterate through all items in list. """
        node_count = 0                              # Node counter initialized to zero
        node = self.head                            # Start at head node

        # Loop until the node is None, which is one node too far past the tail
        while node:
            node_count += 1                         # Increment node counter
            node = node.next                        # Skip to next node
        return node_count

    def get_at_index(self, index):
        """ Returns item at given index in linked list, or
        raises ValueError if given index is out of range of list size.\n
        BEST CASE = O(1) --> Gets index at head of list.\n
        WORST CASE = O(n) --> Gets index at tail of list. """
        # Checks if given index is out of range, and if so, raises error
        if not (0 <= index < self.size):
            raise ValueError("\nLIST INDEX OUT OF RANGE: {}\n".format(index))
        
        node_index, node = 0, self.head
        _data_ = node.data

        # Loop until node index matches input index, then return data
        while node_index < index:
            node_index += 1                         # Increment node counter
            node = node.next                        # Skip to next node
            _data_ = node.data                      # Grab next node's data
        return _data_

    def insert_at_index(self, index, item):
        """ Inserts given item at given index in linked list, or
        raises ValueError if given index is out of range of list size.\n
        BEST CASE = O(1) --> Inserts item at head of list.\n
        WORST CASE = O(n) --> Inserts item in middle of list. """
        # TODO: Use .get_at_index() for clarity
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError("\nLIST INDEX OUT OF RANGE: {}\n".format(index))
        
        # Instantiates Node object and increments size
        node = Node(item)

        # Checks base case where head is not defined, then creates head and tail
        if self.head is None:
            self.head = self.tail = node            # Sets head and tail to single node
            self.size += 1   
        # Inserts item at head, redefines item as head, and points head to next
        # TODO: Use .prepend() method for clarity
        elif index == 0:
            # _head_ = self.head
            # node.next = _head_
            # self.head = node
            self.prepend(node.data)
        # Inserts item at tail, redefines item as tail, and points previous item to tail
        # TODO: Use .append() method for clarity
        elif index == self.size - 1:
            # _tail_ = self.tail
            # _tail_.next = node
            # self.tail = node
            self.append(node.data)
        # Inserts item anywhere else and defines pointers to and from item
        else:
            node_index = 0
            _curr_ = self.head                      # Sets head to current position
            _next_ = _curr_.next                    # Moves next pointer ahead

            # Loops through while indices are unequal to define node placement
            while node_index < index:
                if index == node_index - 1:         # Check if index is at end of list
                    _curr_.next = node
                    node.next = _next_
                    self.size += 1
                    return
                node_index += 1                     # Increment node index

    def append(self, item):
        """ Inserts given item at tail of linked list.\n
        BEST/WORST CASE: O(1) --> Inserts item at tail if exists or as tail if not. """
        new_node = Node(item)                       # Creates new node to hold given item

        # Checks if linked list is empty
        if self.is_empty():
            self.head = new_node                    # Assigns head to new node
        else:
            self.tail.next = new_node               # Inserts new node after tail
        self.tail = new_node                        # Updates tail to new node
        self.size += 1

    def prepend(self, item):
        """ Inserts given item at head of linked list.\n
        BEST/WORST CASE: O(1) --> Inserts item at head if exists or as head if not. """
        new_node = Node(item)                       # Creates new node to hold given item

        # Checks if linked list is empty
        if self.is_empty():
            self.tail = new_node                    # Assigns tail to new node
        else:
            new_node.next = self.head               # Inserts new node before head
        self.head = new_node                        # Updates head to new node
        self.size += 1

    def find(self, quality):
        """ Returns item from linked list satisfying given quality.\n
        BEST CASE = O(1) --> Finds item at head of list.\n
        WORST CASE = O(n) --> Finds item at tail of list. """
        node = self.head                            # Start at head node (constant time)

        # Loop until the node is None, which is one node too far past the tail
        while node:                                 # Up to n iterations
            if quality(node.data):                  # Check if node data matches quality (constant time)
                return node.data
            node = node.next                        # Skips to next node (constant time)
        return None

    def replace(self, old_item, new_item):
        """ Replaces given old_item in linked list with given new_item
        using same node, or raises ValueError if old_item is not found.\n
        BEST CASE: O(1) --> Replaces item at head.\n
        WORST CASE: O(n) --> Replaces item at tail. """
        _tail_ = self.tail                          # Defines tail node

        # Checks if tail data is match, otherwise loops through all nodes for potential data match
        if _tail_.data == old_item:
            _tail_.data = new_item
        else:
            node = self.head                        # Moves node to head
            while node:
                if node.data == old_item:           # Checks for data match on each node
                    node.data = new_item
                    return
                else:
                    node = node.next                # Moves to next node
            raise ValueError("\nERROR: ITEM NOT FOUND -> {}\n".format(old_item))

    def delete(self, item):
        """ Deletes given item from linked list, or raises ValueError.\n
        BEST CASE = O(1) --> Deletes item at head of list.\n
        WORST CASE = O(n) --> Deletes item at tail of list. """
        # TODO: Use .find()
        node = self.head                            # Start at head node
        # Keeps track of node before item-containing node and creates flag for finding given item
        _prev_, is_found = None, False    

        # Loop until we have found the given item or the node is None
        while not is_found and node:
            if node.data == item:                   # Check if node's data matches given item
                is_found = True                     # Update found flag to True
            else:
                _prev_ = node           
                node = node.next                    # Skip to next node

        # Check if we found given item or not and reached tail
        if is_found:
            # Check if we found node in middle of linked list
            if node is not self.head and node is not self.tail:
                _prev_.next = node.next             # Update previous node to skip around found node
                node.next = None                    # Unlink found node from next node
            # Check if we found a node at the head
            if node is self.head:
                self.head = node.next               # Update head to next node
                node.next = None                    # Unlink found node from next node
            # Check if we found a node at the tail
            if node is self.tail:
                if _prev_:                          # Check if there is node before found node
                    _prev_.next = None              # Unlink previous node from found node
                self.tail = _prev_                  # Update tail to previous node
            self.size -= 1                          # Decrement size
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError("\nITEM NOT FOUND: {}\n".format(item))


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    print('Getting items by index:')
    for index in range(ll.size):
        item = ll.get_at_index(index)
        print('get_at_index({}): {!r}'.format(index, item))

    print('Deleting items:')
    ll.delete('B')
    print(ll)
    ll.delete('C')
    print(ll)
    ll.delete('A')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
