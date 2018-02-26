#!python

# ================================== GLOBAL IMPORT STATEMENTS ====================================

import sys

# ===================== FUNCTION TO PERFORM LINEAR SEARCH ON LIST OF ITEMS =======================
def linear_search(array, item):
    """ Returns first index of item in array or None if item is not found. """
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)

# ======================= FUNCTION TO ITERATIVELY PERFORM LINEAR SEARCH ==========================
# TIME COMPLEXITY:  O(n)
# SPACE COMPLEXITY: ???
def linear_search_iterative(array, item):
    """ Iteratively searches through array using linear search for item-value match. """
    for index, value in enumerate(array):
        if item == value:
            return index        # Item is found
    return None                 # Item is not found

# ======================= FUNCTION TO RECURSIVELY PERFORM LINEAR SEARCH ==========================
# TIME COMPLEXITY:  O(n)
# SPACE COMPLEXITY: ???
def linear_search_recursive(array, item, index=0):
    """ Recursively searches through array using linear search for item-value match. """
    if index < len(array):
        if item == array[index]:
            return index        # Item is found
        else:
            return linear_search_recursive(array, item, index + 1)  # Recursive call
    return None                 # Item is not found

# ===================== FUNCTION TO PERFORM BINARY SEARCH ON LIST OF ITEMS =======================
def binary_search(array, item):
    """ Returns index of item in sorted array or None if item is not found. """
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)

# ======================= FUNCTION TO ITERATIVELY PERFORM BINARY SEARCH ==========================
# TIME COMPLEXITY:  O(log(n))
# SPACE COMPLEXITY: ???
def binary_search_iterative(array, item):
    """ Iteratively searches through array using binary search for item-value match. """
    left_bound, right_bound = 0, len(array) - 1

    # Only iterates when iteration range is mathematically valid
    while left_bound <= right_bound:
        bisector = round(left_bound + (right_bound - left_bound) / 2)   # Sets midpoint bisector

        if array[bisector] == item:         # Returns index if item-value match
            return bisector
        elif array[bisector] < item:        # Ignores left half if item is greater than value
            left_bound = bisector + 1
        else:                               # Ignores right half if item is less than value
            right_bound = bisector - 1

    return None

# ======================= FUNCTION TO RECURSIVELY PERFORM BINARY SEARCH ==========================
# TIME COMPLEXITY:  O(log(n))
# SPACE COMPLEXITY: ???
def binary_search_recursive(array, item, left_bound=None, right_bound=None):
    """ Recursively searches through array using binary search for item-value match. """
    if left_bound is None:
        left_bound = 0
    if right_bound is None:
        right_bound = len(array) - 1

    # Only recurses when recursion range is mathematically valid
    if right_bound >= left_bound:
        bisector = round(left_bound + (right_bound - left_bound) / 2)   # Sets midpoint bisector

        if array[bisector] == item:         # Returns index if item-value match
            return bisector
        elif array[bisector] > item:        # Ignores right half if item is less than value
            return binary_search_recursive(array, item, left_bound, bisector - 1)
        else:                               # Ignores left half if item is greater than value
            return binary_search_recursive(array, item, bisector + 1, right_bound)
    
    return None

# ====================================== MAIN RUN FUNCTION =======================================
def main():
    """ Main run function. """
    args, array = sys.argv[1:], ["Aakash", "Alirie", "Duncan", "Egon", "Matthew", "Yves"]

    if len(args) == 1:
        item = args[0]
        return print("\nINDEX OF ITEM: {}\n".format(binary_search(array, item)))
    else:
        return print("\nUSAGE: {} [item]\n".format(sys.argv[0]))

if __name__ == "__main__":
    main()