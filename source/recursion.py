#!python

# ================================== GLOBAL IMPORT STATEMENTS ====================================

import sys

# ==================== METHOD TO PRODUCE FACTORIAL SUM OF DIGITS 1 THROUGH n =====================

def factorial(n):
    """ Returns the product of the integers 1 through n for n >= 0,
    otherwise raises ValueError for n < 0 or non-integer n """
    if n < 0 or not isinstance(n, int):
        raise ValueError("FACTORIAL MULTIPLICATIVE RANGE IS UNDEFINED FOR n = {}".format(n))
    # return factorial_recursive(n)
    return factorial_iterative(n)

# ======================= METHOD TO CALCULATE ITERATIVE FACTORIAL PRODUCT ========================

def factorial_iterative(n):
    """ Iteratively multiplies integers from 1 against its increments until i = n. """
    if n == 0:
        return 1
    elif n > 0:
        iterative_product = 1
        for iterator in range(2, n + 1):
            iterative_product *= iterator
    return iterative_product

# ======================= METHOD TO CALCULATE RECURSIVE FACTORIAL PRODUCT ========================

def factorial_recursive(n):
    """ Recursively multiplies n against its decrements until n = 0, 1. """
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return n * factorial_recursive(n - 1)

# ====================================== MAIN RUN FUNCTION =======================================

def main():
    """ Main run function for factorial product summation. """
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 1:
        num = int(args[0])
        result = factorial(num)
        print("\nFACTORIAL({}) => {}\n".format(num, result))
    else:
        print("\nUSAGE: {} [number]\n".format(sys.argv[0]))

if __name__ == '__main__':
    main()
