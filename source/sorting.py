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
    """ Merges given lists of items, each assumed to already be in sorted order,
    and returns new list containing all items in sorted order.\n
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
        merged_list.extend(items1[iterator1:])
    # Checks if second list is non-empty
    else:
        # Adds remaining elements from second list to merged list
        merged_list.extend(items2[iterator2:])
    return merged_list


def split_sort_merge(items):
    """ Sorts given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    list in sorted order.\n
    RUNTIME (BEST):     O(1) -> Array is single or empty.\t
    RUNTIME (WORST):    O(n^2) -> Iterate through array length proportionally by array length.\t
    MEMORY:             O(n) -> Rewrite every value in array."""
    LENGTH_ITEMS = len(items)                       # Initializes length of list
    bisector = LENGTH_ITEMS // 2                    # Defines approximate midpoint of list

    # Defines left and right split halves by midpoint bisection
    left_half, right_half = items[:bisector], items[bisector:]
    
    # Sorts both halves by passing halves through choice sorting algorithm (Binary Insertion Sort)
    sorted_left_half, sorted_right_half = insertion_sort(left_half, True), insertion_sort(right_half, True)
    return merge(sorted_left_half, sorted_right_half)

def merge_sort(items):
    """ Sorts given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into list in sorted order.\n
    RUNTIME (BEST):     O(1) -> List contains one item. \t
    RUNTIME (WORST):    O(n * log(n)) -> Logarithmically sorts all items per item in list.\t
    MEMORY:             O(n) -> Recursively splits, then merges list of n items. """
    # TODO: Consider using NumPy arrays to reduce memory costs of copying references with slices
    LENGTH_ITEMS = len(items)                       # Initializes length of list
    if LENGTH_ITEMS < 2:                           # Recursion endgame when split list contains one item
        return items
    bisector = LENGTH_ITEMS // 2                    # Defines approximate midpoint of list

    # Defines left and right split halves by midpoint bisection
    left_half, right_half = items[:bisector], items[bisector:]

    merge_sort(left_half); merge_sort(right_half)
    # Recursively sorts both halves by passing halves through merge sorting algorithm (logarithmic reduction)
    items[:] = merge(left_half, right_half)

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    RUNTIME (BEST):     O(?)\t
    RUNTIME (WORST):    O(?)\t
    MEMORY:             O(?) """
    pivot = low                                     # Defines pivot item as lower index
    for iterator in range(low + 1, high + 1):       # Iterates across incremented partitioned range
        if items[iterator] <= items[low]:           # Checks if current item is less than or equal to lower indexed item
            pivot += 1                              # Increments pivot item and swaps current and pivoting elements
            items[iterator], items[pivot] = items[pivot], items[iterator]

    # Swaps pivoting and lower indexed elements, then returns pivot item
    items[pivot], items[low] = items[low], items[pivot]
    return pivot

def quick_sort(items, low=None, high=None):
    """ Sorts given items in place by partitioning items in range `[low...high]`
    around pivot item and recursively sorting each remaining sublist range.\n
    RUNTIME (BEST):     O(?)\t
    RUNTIME (WORST):    O(?)\t
    MEMORY:             O(?) """
    if low is None:                                 # Checks if low index is undefined
        low = 0                                     # Defines low index as zero
    if high is None:                                # Checks if high index is undefined
        high = len(items)                           # Defines high index as list length 
    if low >= high:                                 # Checks if [low, high] range is mathematically invalid
        return items                                # Return empty/invalid list
    if low < high:                                  # Checks if [low, high] range is mathematically valid
        pivot = partition(items, low, high)         # Partitions list and returns pivot item
        quick_sort(items, low, pivot - 1)           # Recursively sorts on lower pivoted sublist
        quick_sort(items, pivot + 1, high)          # Recursively sorts on higher pivoted sublist
    return items



def counting_sort(numbers):
    # FIXME: Improve this to mutate input instead of creating new output list
    """ Sorts given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.\n
    RUNTIME (BEST):     O(?)\t
    RUNTIME (WORST):    O(?)\t
    MEMORY:             O(?) """
    # Initializes absolute maxima and minima of numerical list and produces empty counts array
    absolute_maximum, absolute_minimum = max(numbers), min(numbers)
    histocounts = [0] * (absolute_maximum - absolute_minimum + 1)

    for number in numbers:                          # Iterates across list of numbers
        histocounts[number - absolute_minimum] += 1 # Creates histogram of number occurrences

    sorted_numbers = list()                         # Initializes sorted numbers array

    # Iterates across range of possible numbers in list
    for outer_iterator in range(absolute_minimum, absolute_maximum + 1):
        # Checks if counts position has at least one occurrence
        if histocounts[outer_iterator - absolute_minimum] > 0:
            # Iterates across range of occurrences of current number in original list
            for inner_iterator in range(histocounts[outer_iterator - absolute_minimum]):
                # Appends all occurrences of current number to sorted array
                sorted_numbers.append(outer_iterator)
    return sorted_numbers


def bucket_sort(numbers, num_buckets=10):
    # FIXME: Improve this to mutate input instead of creating new output list
    """ Sorts given numbers by distributing into buckets representing subranges,
    sorting each bucket, and combining contents of all buckets in sorted order.\n
    RUNTIME (BEST):     O(1) -> ???\t
    RUNTIME (WORST):    O(n^2) -> ???\t
    MEMORY:             O(n + k) -> ??? """
    # Initializes absolute maxima and minima of numerical list
    absolute_minimum, absolute_maximum = min(numbers), max(numbers)
    LENGTH_ITEMS = len(numbers)                     # Initializes original list length

    buckets = [list() for _ in range(num_buckets)]  # Initializes and creates list of buckets
    for iterator in range(LENGTH_ITEMS):            # Iterates across original list
        # Creates bucket position based on value of current list number and appends number to bucket
        bucket = int(num_buckets * numbers[iterator])
        buckets[bucket].append(numbers[iterator])
    LENGTH_BUCKETS = len(buckets)                   # Initializes length of bucket list

    for iterator in range(LENGTH_BUCKETS):          # Iterates across buckets
        insertion_sort(buckets[iterator], True)     # Performs binary insertion sort on items in each bucket

    sorted_numbers = list()                         # Initializes sorted numbers list
    for iterator in range(LENGTH_BUCKETS):          # Iterates across buckets
        while len(buckets[iterator]) > 0:           # Iterates while current bucket is not empty
            # Pops bucket values from bucket list and into sorted list while current bucket is not empty
            sorted_numbers.append(buckets[iterator].pop(0))
    return sorted_numbers

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
