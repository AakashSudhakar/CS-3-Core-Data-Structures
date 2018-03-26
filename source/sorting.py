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

    if not reverse:                                 # Checks if list should be forward sorted
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

    if not reverse:                                 # Checks if list should be forward sorted
        for outer_iterator in range(LENGTH_ITEMS):  # Loops through array and checks each item against array
            for inner_iterator in range(outer_iterator, LENGTH_ITEMS):
                if items[inner_iterator] < items[outer_iterator]:
                    items[inner_iterator], items[outer_iterator] = items[outer_iterator], items[inner_iterator]
        return items
    else:                                           # Checks if list should be reverse sorted
        for outer_iterator in range(LENGTH_ITEMS):  # Loops through array and checks each item against array
            for inner_iterator in range(outer_iterator, LENGTH_ITEMS):
                if items[inner_iterator] >= items[outer_iterator]:
                    items[inner_iterator], items[outer_iterator] = items[outer_iterator], items[inner_iterator]
        return items

def cocktail_shaker_sort(items):
    """ Sorts given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.\t
    Similar to Bubble Sort except bounces back and forth across array.\n
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

def selection_sort(items, reverse=False):
    """ Sorts given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.\n
    RUNTIME (BEST):     O(1) -> Array is single or empty.\t
    RUNTIME (WORST):    O(n^2) -> Iterate through array length proportionally by array length.\t
    MEMORY:             O(n) -> Rewrite every value in array."""
    LENGTH_ITEMS = _validate_list_of_items(items)   # Validates items object type and returns list length
    # NOTE: Base case where LENGTH_ITEMS = 0, 1 are covered naturally by range()

    if not reverse:                                 # Checks if list should be forward sorted
        for outer_iterator in range(LENGTH_ITEMS):  # Loops through item array checking for local minima
            for inner_iterator in range(outer_iterator, LENGTH_ITEMS):
                # If unsorted minimum value is detected, swap with first unsorted item and continue iterating
                if items[inner_iterator] < items[outer_iterator]:
                    local_minimum, items[inner_iterator], items[outer_iterator] = items[inner_iterator], items[outer_iterator], local_minimum
        return items
    else:                                           # Checks if list should be reverse sorted
        for outer_iterator in range(LENGTH_ITEMS):  # Loops through item array checking for local minima
            for inner_iterator in range(outer_iterator, LENGTH_ITEMS):
                # If unsorted minimum value is detected, swap with first unsorted item and continue iterating
                if items[inner_iterator] >= items[outer_iterator]:
                    local_minimum, items[inner_iterator], items[outer_iterator] = items[inner_iterator], items[outer_iterator], local_minimum
        return items

def insertion_sort(items, with_bin=False):
    """ Sorts given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.\n
    RUNTIME (BEST):     O(1) -> Array is single or empty.\t
    RUNTIME (WORST):    O(n^2) -> Iterate through array length proportionally by array length.\t
    MEMORY:             O(n) -> Rewrite every value in array."""
    LENGTH_ITEMS = _validate_list_of_items(items)   # Validates items object type and returns list length
    # NOTE: Base case where LENGTH_ITEMS = 0, 1 are covered naturally by range()

    if not with_bin:
        for index, item in enumerate(items):        # Enumerates through item array
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
        for index, item in enumerate(items):        # Enumerates through item array
            lower_bound, upper_bound = 0, index     # Defines lower and upper boundaries
            while upper_bound > lower_bound:
                bisector = (lower_bound + upper_bound) // 2
                if items[bisector] < item:
                    lower_bound = bisector + 1
                else:
                    upper_bound = bisector
            items[:] = items[:lower_bound] + [item] + items[lower_bound:index] + items[index + 1:]
        return items
    # TODO: Implement reverse order sorting algorithm. 

# NOTE: What have I done?!
def library_sort(items):
    """ (Gapped Insertion Sort) Sorts given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.\t
    Similar to Insertion Sort but with gaps (bitwise) in array to accelerate subsequent insertions.\n
    RUNTIME (BEST):     O(n)\t
    RUNTIME (WORST):    O(n * log(n))\t
    MEMORY:             O(trash) """
    LENGTH_ITEMS = _validate_list_of_items(items)   # Validates items object type and returns list length
    # NOTE: Base case where LENGTH_ITEMS = 0, 1 are covered naturally by range()
    gapped_insertions = [None] * (LENGTH_ITEMS << 1)
    BITLENGTH_ITEMS = LENGTH_ITEMS.bit_length()     # Initializes bitwise lengths for advanced gapped item manipulation

    # Produces list of gaps that hold preset gap indices over original data for gapped insertions
    for iterator in range(LENGTH_ITEMS):
        gapped_insertions[2 * iterator + 1] = gap_list[iterator]

    # Predefines lower and upper bounds for bitwise comparator constants
    lesser_bitwise_comparator, greater_bitwise_comparator = 1, 2

    # Iterates over bitwise length of original array
    for outer_iterator in range(BITLENGTH_ITEMS):
        # Shifts bits of comparator constants for each iteration
        lesser_bitwise_comparator <<= 1
        greater_bitwise_comparator <<= 1

        # Iterates over inner bitwise range for each item
        for inner_iterator in range(lesser_bitwise_comparator, min(greater_bitwise_comparator, LENGTH_ITEMS + 1)):
            gapped_max_position = 2 * inner_iterator - 1
            gapped_item = gapped_insertions[gapped_max_position]
            lower_bound, upper_bound = 0, gapped_max_position

            while upper_bound - lower_bound > 1:
                shifted_boundary_range = (lower_bound + upper_bound) >> 1

                if gapped_insertions[shifted_boundary_range] != None:
                    if gapped_insertions[shifted_boundary_range] < gapped_item:
                        lower_bound = shifted_boundary_range
                    else:
                        upper_bound = shifted_boundary_range
                else:
                    shifted_lower_bound, shifted_upper_bound = shifted_boundary_range - 1, shifted_boundary_range + 1
                    while gapped_insertions[shifted_lower_bound] == None:
                        shifted_lower_bound -= 1
                    while gapped_insertions[shifted_upper_bound] == None:
                        shifted_upper_bound += 1
                    if gapped_insertions[shifted_lower_bound] > gapped_item:
                        upper_bound = shifted_lower_bound
                    elif gapped_insertions[shifted_upper_bound] < gapped_item:
                        lower_bound = shifted_upper_bound
                    else:
                        lower_bound, upper_bound = shifted_lower_bound, shifted_upper_bound
                        break

            if upper_bound - lower_bound > 1:
                gapped_insertions[ (lower_bound + upper_bound) >> 1 ] = gapped_item
            else:
                if gapped_insertions[lower_bound] != None:
                    if gapped_insertions[lower_bound] > gapped_item:
                        upper_bound = lower_bound

                    while gapped_item != None:
                        gapped_insertions[upper_bound], gapped_item = gapped_item, gapped_insertions[upper_bound]
                    upper_bound += 1
                else:
                    gapped_insertions[lower_bound] = gapped_item
            gapped_insertions[gapped_max_position] = None

        if greater_bitwise_comparator > LENGTH_ITEMS:
            break
        if outer_iterator < BITLENGTH_ITEMS - 1:
            gapped_item = gapped_max_position

            while gapped_item >= 0:
                if gapped_insertions[gapped_item] != None:
                    gapped_insertions[gapped_item], gapped_insertions[gapped_max_position] = None, gapped_insertions[gapped_item]
                    gapped_max_position -= 2
                gapped_item -= 1
    return [item for item in gapped_insertions if item != None]

def shell_sort(items):
    """ Sorts.\n
    RUNTIME (BEST):     O(?)\t
    RUNTIME (WORST):    O(?)\t
    MEMORY:             O(?) """
    LENGTH_ITEMS = _validate_list_of_items(items)   # Validates items object type and returns list length
    # NOTE: Base case where LENGTH_ITEMS = 0, 1 are covered naturally by range()
    midpoint = LENGTH_ITEMS / 2

    while midpoint:
        for index, item in enumerate(items):
            position = index
            while position >= midpoint and items[position - midpoint] > item:
                items[position] = items[position - midpoint]
                position -= midpoint
            items[position] = item
        midpoint = (midpoint / 2) if (midpoint / 2) else (0 if midpoint == 1 else 1)
    return items

def merge(items1, items2):
    """ Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    RUNTIME (BEST):     O(1) -> Both lists contain one item. \t
    RUNTIME (WORST):    O(max(N, M)) -> Iterates over maximum length between both lists. \t
    MEMORY:             O(N + M) -> Creates new list containing all elements of both lists. """
    iterator1, iterator2 = 0, 0                     # Initializes iterators and lengths of both lists
    LENGTH_ITEMS1, LENGTH_ITEMS2 = len(items1), len(items2)
    merged_list = list()                            # Initializes returning merged list from both lists

    # Loops over both lists (N * M) comparing each pair of indexed elements
    while iterator1 < LENGTH_ITEMS1 and iterator2 < LENGTH_ITEMS2:
        # Defines local minima and initializes absolute minimum between both sorted list items
        local_minimum1, local_minimum2 = items1[iterator1], items2[iterator2]
        absolute_minimum = 0

        # Checks if first list's local minimum is less than second list's local minimum
        if local_minimum1 < local_minimum2:
            absolute_minimum = local_minimum1       # Sets absolute minimum to local minimum of first list
            merged_list.append(absolute_minimum)    # Appends absolute minimum to merged list
            iterator1 += 1                          # Increments first list's iterator
        # Checks if second list's local minimum is less than or equal to first list's local minimum
        else:
            absolute_minimum = local_minimum2       # Sets absolute minimum to local minimum of second list
            merged_list.append(absolute_minimum)    # Appends absolute minimum to merged list
            iterator2 += 1                          # Increments second list's iterator

    # Checks if first list is non-empty
    if iterator1 != LENGTH_ITEMS1:
        # Adds remaining elements from first list to merged list
        merged_list.extend(items1[iterator1:LENGTH_ITEMS1])
    # Checks if second list is non-empty
    else:
        # Adds remaining elements from second list to merged list
        merged_list.extend(items2[iterator2:LENGTH_ITEMS2])
    return merged_list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    RUNTIME (BEST):     O(?)\t
    RUNTIME (WORST):    O(?)\t
    MEMORY:             O(?) """
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    RUNTIME (BEST):     O(?)\t
    RUNTIME (WORST):    O(?)\t
    MEMORY:             O(?) """
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    RUNTIME (BEST):     O(?)\t
    RUNTIME (WORST):    O(?)\t
    MEMORY:             O(?) """
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    RUNTIME (BEST):     O(?)\t
    RUNTIME (WORST):    O(?)\t
    MEMORY:             O(?) """
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    RUNTIME (BEST):     O(?)\t
    RUNTIME (WORST):    O(?)\t
    MEMORY:             O(?) """
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    sorting each bucket, and combining contents of all buckets in sorted order.
    RUNTIME (BEST):     O(?)\t
    RUNTIME (WORST):    O(?)\t
    MEMORY:             O(?) """
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
