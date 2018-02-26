#!python

# ================================== GLOBAL IMPORT STATEMENTS ====================================

import sys

# ============= FUNCTION TO IMPLEMENT HEAP'S ALGORITHM FOR GENERATING PERMUTATIONS ===============
def generate_permutations_heap(array):
    """ Returns list of possible permutations of inputted string of chars. """
    # return generate_permutations_heap_iterative(len(array), array)
    return generate_permutations_heap_recursive(len(array), array)

# ====================== FUNCTION TO ITERATIVELY PERFORM HEAP'S ALGORITHM ========================
def generate_permutations_heap_iterative(n, array):
    """ Iteratively generates permutations from string data. """
    pass

# ====================== FUNCTION TO RECURSIVELY PERFORM HEAP'S ALGORITHM ========================
def generate_permutations_heap_recursive(n, array):
    """ Recursively generates permutations from string data. """
    if n == 0:
        return array
    else:
        for iterator in range(n - 1):
            return generate_permutations_heap_recursive(n - 1, array)
            
            if iterator % 2 == 0:
                swap_elements(array, iterator, n - 1)
            else:
                swap_elements(array, 0, n - 1)
            
        return generate_permutations_heap_recursive(n - 1, array)

# ========================= FUNCTION TO SWAP PERMUTATION DATA BY INDEX ===========================
def swap_elements(array, i, j):
    """ Swaps permutation data entries in array across Heap's Algorithm implementation. """
    array[i], array[j] = array[j], array[i]

# ===================================== MAIN RUN FUNCTION ========================================
def main():
    """ Main run function. """
    args = sys.argv[1:]

    if len(args) == 1:
        permutations = args[0]
        return print("\nPERMUTATIONS ARE AS FOLLOWS:\n\n{}".format(generate_permutations_heap(permutations)))
    else:
        return print("\nUSAGE: {} [str_arr]\n".format(sys.argv[0]))

if __name__ == "__main__":
    main()