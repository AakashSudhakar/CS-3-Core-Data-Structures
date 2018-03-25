#!python

from timeit import timeit

def is_sorted(items, reverse=False):
    """ Returns boolean indicating whether given items are in sorted order.\n
    RUNTIME (BEST):     O(1) -> Single or empty array.\t
    RUNTIME (WORST):    O(n) -> Iterates across entire array.\t
    MEMORY:             O(1) -> Creates single element to store length."""
    assert isinstance(reverse, bool)                # Asserts that reverse parameter is boolean
    LENGTH_ITEMS = len(items)                       # Defines length of item array
    # NOTE: Base case where LENGTH_ITEMS = 0, 1 are covered naturally by range()

    if reverse is False:                            # Checks if list should be forward sorted
        for index in range(1, LENGTH_ITEMS):        # Loops through length of array
            if items[index - 1] > items[index]:     # Checks if previous item is greater than current item
                return False                        # Returns False if current condition is True, else returns True
        return True
    else:                                           # Checks if list should be reverse sorted
        for index in range(1, LENGTH_ITEMS):        # Loops through length of array
            if items[index] < items[index + 1]:     # Checks if current item is less than next item
                return False                        # Returns False if current condition is True, else returns True
        return True

def _validate_list_of_items(items):
    """ Helper function that validates type of items object and returns object array length. """
    assert isinstance(items, list)                  # Asserts that items object is list
    return len(items)                               # Defines length of item array

def bubble_sort(items, reverse=False):
    """ Sorts given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.\n
    RUNTIME (BEST):     O(n) -> Iterate through sorted array once.\t
    RUNTIME (WORST):    O(n^2) -> Iterate through array length proportionally by array length.\t
    MEMORY:             O(1) -> Doesn't create new memory but rewrites current memory. """
    assert isinstance(reverse, bool)                # Asserts that reverse parameter is boolean
    LENGTH_ITEMS = _validate_list_of_items(items)   # Validates items object type and returns list length
    # NOTE: Base case where LENGTH_ITEMS = 0, 1 are covered naturally by range()

    if reverse is False:                            # Checks if list should be forward sorted
        for outer_iterator in range(LENGTH_ITEMS):  # Loops through array and checks each item against array
            for inner_iterator in range(outer_iterator, LENGTH_ITEMS):
                # If items are out-of-order, swaps them and continues
                if items[inner_iterator] < items[outer_iterator]:
                    items[inner_iterator], items[outer_iterator] = items[outer_iterator], items[inner_iterator]
        return items
    else:                                           # Checks if list should be reverse sorted
        for outer_iterator in range(LENGTH_ITEMS):  # Loops through array and checks each item against array
            for inner_iterator in range(outer_iterator, LENGTH_ITEMS):
                # If items are out-of-order, swaps them and continues
                if items[inner_iterator] >= items[outer_iterator]:
                    items[inner_iterator], items[outer_iterator] = items[outer_iterator], items[inner_iterator]
        return items

    def cocktail_shaker_sort(items, reverse=False):
        """ Sorts given items by swapping adjacent items that are out of order, and
        repeating until all items are in sorted order. Similar to Bubble Sort except
        bounces back and forth across array.\n
        RUNTIME (BEST):     O(n) -> Iterate through sorted array once.\t
        RUNTIME (WORST):    O(n^2) -> Iterate through array length proportionally by array length.\t
        MEMORY:             O(1) -> Doesn't create new memory but rewrites current memory. """
        assert isinstance(reverse, bool)                # Asserts that reverse parameter is boolean
        LENGTH_ITEMS = _validate_list_of_items(items)   # Validates items object type and returns list length
        # NOTE: Base case where LENGTH_ITEMS = 0, 1 are covered naturally by range()

        # Loops through all items in array in reverse order
        for outer_iterator in range(LENGTH_ITEMS, 0, -1):
            is_swapped = False                          # Creates parameter to track swapped items
            
            # Checks each item against rest of array in reverse order and swaps if out-of-order
            for inner_iterator in range(outer_iterator, 0, -1):
                if items[inner_iterator] < items[inner_iterator - 1]:
                    items[inner_iterator], items[inner_iterator - 1] = items[inner_iterator - 1], items[inner_iterator]
                    is_swapped = True

            # Checks each item against rest of array in forward order and swaps if out-of-order
            for inner_iterator in range(outer_iterator):
                if items[inner_iterator] > items[inner_iterator + 1]:
                    items[inner_iterator], items[inner_iterator + 1] = items[inner_iterator + 1], items[inner_iterator]
                    is_swapped = True

            # Returns items when no swapping options left
            if not is_swapped:
                return items

def selection_sort(items):
    """ Sorts given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.\n
    RUNTIME (BEST):     O(1) -> Array is single or empty.\t
    RUNTIME (WORST):    O(n^2) -> Iterate through array length proportionally by array length.\t
    MEMORY:             O(n) -> Rewrite every value in array."""
    LENGTH_ITEMS = _validate_list_of_items(items)   # Validates items object type and returns list length
    # NOTE: Base case where LENGTH_ITEMS = 0, 1 are covered naturally by range()

    # Loops through item array checking for local minima
    for outer_iterator in range(LENGTH_ITEMS):
        for inner_iterator in range(outer_iterator, LENGTH_ITEMS):
            # If unsorted minimum value is detected, swap with first unsorted item and continue iterating
            if items[inner_iterator] < items[outer_iterator]:
                local_minimum, items[inner_iterator], items[outer_iterator] = items[inner_iterator], items[outer_iterator], local_minimum
    return items

    # TODO: Implement reverse order sorting algorithm. 


def insertion_sort(items, with_binary_search=False):
    """ Sorts given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.\n
    RUNTIME (BEST):     O(1) -> Array is single or empty.\t
    RUNTIME (WORST):    O(n^2) -> Iterate through array length proportionally by array length.\t
    MEMORY:             O(n) -> Rewrite every value in array."""
    LENGTH_ITEMS = _validate_list_of_items(items)   # Validates items object type and returns list length
    if LENGTH_ITEMS < 2:                            # Checks if array has single or no values
        return items                                # If True, returns items as array is naturally sorted

    if with_binary_search is False:
        # Enumerates through item array
        for index, item in enumerate(items):
            position = index
            # Checks if current position is positive and current item is out-of-order
            while position > 0 and item < items[position - 1]:
                # If True, swap item with previous item and decrement position
                items[position] = items[position - 1]
                position -= 1
            # Redefines current position in array to current item
            items[position] = item
        return items
    else:
        # TODO: Implement Insertion Sort variation with Binary Search here. 
        return items

    # TODO: Implement reverse order sorting algorithm. 

def library_sort(items):
    """ Sorts.\n
    RUNTIME (BEST):     O(?)\t
    RUNTIME (WORST):    O(?)\t
    MEMORY:             O(?) """
    LENGTH_ITEMS = _validate_list_of_items(items)   # Validates items object type and returns list length
    if LENGTH_ITEMS < 2:                            # Checks if array has single or no values
        return items                                # If True, returns items as array is naturally sorted

    # TODO: Implement Library Sorting algorithm here. 
    return items

def shell_sort(items):
    """ Sorts.\n
    RUNTIME (BEST):     O(?)\t
    RUNTIME (WORST):    O(?)\t
    MEMORY:             O(?) """
    LENGTH_ITEMS = _validate_list_of_items(items)   # Validates items object type and returns list length
    if LENGTH_ITEMS < 2:                            # Checks if array has single or no values
        return items                                # If True, returns items as array is naturally sorted

    # TODO: Implement Shell Sorting algorithm here. 
    return items


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    sorting each bucket, and combining contents of all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    # sort = bubble_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


if __name__ == '__main__':
    main()
