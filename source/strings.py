#!python

def contains(text, pattern):
    """ Returns boolean indicating whether pattern occurs in text. """
    assert isinstance(text, str), "\nTEXT IS NOT A STRING: {}\n".format(text)
    assert isinstance(pattern, str), "\nPATTERN IS NOT A STRING: {}\n".format(text)

    if find_index(text, pattern) is not None:
        return True
    return False

def find_index(text, pattern, text_index = 0, pattern_index = 0):
    """ Returns starting index of first occurrence of pattern in text,
    or None if not found. """
    # NOTE: Recursive implementation of find_index()
    assert isinstance(text, str), "\nTEXT IS NOT A STRING: {}\n".format(text)
    assert isinstance(pattern, str), "\nPATTERN IS NOT A STRING: {}\n".format(text)

    if pattern == "":
        return pattern_index
    if pattern_index == len(pattern):
        return text_index - len(pattern)
    if text_index == len(text):
        return None
    if text[text_index] == pattern[pattern_index]:
        return find_index(text, pattern, text_index + 1, pattern_index + 1)
    if pattern_index == 0:
        return find_index(text, pattern, text_index + 1, pattern_index)
    return find_index(text, pattern, text_index - pattern_index + 1, 0)

def find_all_indices(text, pattern, t_index = 0, p_index = 0, found_indices = None):
    """ Returns list of starting indices of all occurrences of pattern in text,
    or empty list if not found. """
    # NOTE: Recursive implementation of find_all_indices()
    assert isinstance(text, str), "\nTEXT IS NOT A STRING: {}".format(text)
    assert isinstance(pattern, str), "\nPATTERN IS NOT A STRING: {}".format(text)

    if found_indices is None:
        found_indices = []
    if pattern == "":
        if t_index >= len(text):
            return found_indices
        found_indices.append(t_index - len(pattern))
        return find_all_indices(text, pattern, t_index + 1, 0, found_indices)
    if p_index >= len(pattern):
        found_indices.append(t_index - len(pattern))
        return find_all_indices(text, pattern, t_index - len(pattern) + 1, 0, found_indices)
    if t_index >= len(text):
        return found_indices
    if text[t_index] == pattern[p_index]:
        return find_all_indices(text, pattern, t_index + 1, p_index + 1, found_indices)
    if p_index == 0:
        return find_all_indices(text, pattern, t_index + 1, 0, found_indices)
    return find_all_indices(text, pattern, t_index, 0, found_indices)

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indices
    indexes = find_all_indices(text, pattern)
    print('find_all_indices({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indices('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
