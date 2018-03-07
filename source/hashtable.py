#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """ Initializes hash table with given initial size. """
        self.buckets = [LinkedList() for iterator in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """ Returns formatted string representation of hash table. """
        items = ["{!r}: {!r}".format(key, value) for key, value in self.items()]
        return "{" + ", ".join(items) + "}"

    def __repr__(self):
        """ Returns string representation of hash table. """
        return "HashTable({!r})".format(self.items())

    def _bucket_index(self, key):
        """ Returns bucket index where given key would be stored. """
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """ Returns load factor. (Ratio of number of entries to buckets.)\n
        BEST/WORST CASE = O(n) --> Iterates through entire length of Linked List. """
        return self.size / len(self.buckets)

    def keys(self):
        """ Returns list of all keys in hash table.\n
        BEST/WORST CASE = O(m * n) --> Iterate through all items in old and new tables. """
        # Collect all keys in each of the buckets
        all_keys = list()
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """ Returns list of all values in hash table.\n
        BEST/WORST CASE = O(m * n) --> Iterate through all items in old and new tables. """
        # Collect all values in each of the buckets
        all_values = list()
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """ Returns list of all entries (key-value pairs) in hash table.\n
        BEST/WORST CASE = O(m * n) --> Iterate through all items in old and new tables. """
        # Collects all pairs of key-value entries in every bucket
        all_items = list()
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """ Returns number of key-value entries by traversing buckets.\n
        BEST/WORST CASE = O(m * n) --> Iterate through all items in old and new tables. """
        return sum(bucket.length() for bucket in self.buckets)
        # Counts number of key-value entries in every bucket
        # item_count = 0
        # for bucket in self.buckets:
        #     item_count += bucket.length()
        # return item_count

    def contains(self, key):
        """ Returns True if hash table contains given key, or False.\n
        BEST CASE = O(1) --> Target is first item in table.\n
        WORST CASE = O(n) --> Target is last item in table. (Full iteration.) """
        # Finds bucket in which given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Checks if entry with given key exists in given bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None

    def get(self, key):
        """ Returns value associated with given key, or raises KeyError.
        BEST CASE = O(1) --> Target is first item in table.\n
        WORST CASE = O(n) --> Target is last item in table. (Full iteration.) """
        # Finds bucket in which given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Finds entry with given key in given bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:
            # Returns given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:
            raise KeyError("\n\nKEY NOT FOUND: {}\n".format(key))

    def set(self, key, value):
        """ Inserts or updates given key with associated value.\n
        BEST CASE = O(1) --> Target is first item in table.\n
        WORST CASE = O(n) --> Target is last item in table. (Full iteration.) """
        # Finds bucket in which given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Finds the entry with the given key in that bucket, if one exists
        # Checks if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Removes old key-value entry from bucket first
            bucket.delete(entry)
        else:
            self.size += 1
        # Inserts new key-value entry into bucket in either case
        bucket.append((key, value))
        # Resizes hash table if naïve load factor is exceeded
        if self.load_factor() > 0.75:
            self._resize()

    def delete(self, key):
        """ Deletes given key and associated value, or raises KeyError.\n
        BEST CASE = O(1) --> Target is first item in table.\n
        WORST CASE = O(n) --> Target is last item in table. (Full iteration.) """
        # Finds bucket in which given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Finds entry with given key in bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:
            bucket.delete(entry)            # Removes key-value entry from bucket
            self.size -= 1                  # Decrements size
        else:
            raise KeyError("\n\nKEY NOT FOUND: {}\n".format(key))

    def _resize(self, new_size=None):
        """ Resizes hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds threshold
        such as 0.75 after insertion (when set is called with new key).\n
        BEST/WORST CASE = O(m * n) --> Iterate through all items in old and new tables. """
        # If unspecified, chooses new size dynamically based on current size (doubles size)
        if new_size is None:
            new_size = len(self.buckets) * 2
        # Option that reduces size if buckets are sparsely filled (low L.F., halves size)
        elif new_size is 0:
            new_size = len(self.buckets) / 2
        # Temporarily holding array for current hash table items
        current_key_value_entries = self.items()
        # Creates new parameters for resized hash table (more buckets)       
        self.buckets = [LinkedList() for iterator in range(new_size)]
        self.size = 0
        # Places items back into buckets using hashing set method
        for key, value in current_key_value_entries:
            self.set(key, value)


def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()
