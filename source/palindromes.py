#!python

import string
from re import sub

def is_palindrome(text):
    """ Function checks if input string is palindrome (ignores non-alphabetical characters). """
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), "\nINPUT IS NOT A STRING {}".format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)

def is_palindrome_iterative(text):
    """ Iteratively checks using RegEx for alphabetical matching across string by index. """
    text = sub(r"[^a-zA-Z]", "", text).lower()              # RegEx comparative search 
    left, right = 0, len(text) - 1

    # While indices are unequal & converging, check left-right char match (mid doesn't matter)
    while (right > left):
        print("{} ?= {}".format(text[left], text[right]))
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_recursive(text, left=None, right=None):
    """ Recursively checks using RegEx for alphabetical matching across string by index. """
    text = sub(r"[^a-zA-Z]", "", text).lower()              # RegEx comparative search 
    
    if left is None: left = 0
    if right is None: right = len(text) - 1

    # While indices are unequal & converging, check left-right char match (mid doesn't matter)
    while (right > left):
        print("{} ?= {}".format(text[left], text[right]))
        if text[left] != text[right]:
            return False
        # If left-right char match, recursively call function with incremented/decremented L/R indices
        return is_palindrome_recursive(text, left + 1, right - 1)
    return True

def main():
    """ Main run function. """
    import sys
    args = sys.argv[1:]  # Ignore script file name
    
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = "\nPASS" if is_pal else "\nFAIL"
            is_str = "IS" if is_pal else "IS NOT"
            print("{}: {} {} A PALINDROME.\n".format(result, repr(arg), is_str))
    else:
        print("\nUSAGE: {} '[str1] [str2] ... [strN]'".format(sys.argv[0]))
        print("PROGRAM CHECKS IF EACH ARGUMENT GIVEN IS A PALINDROME.\n")

if __name__ == "__main__":
    main()
