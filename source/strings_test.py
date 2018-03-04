#!python

from strings import contains, find_index, find_all_indices
import unittest


class StringsTest(unittest.TestCase):

    def test_contains_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert contains('abc', '') is True  # all strings contain empty string
        assert contains('abc', 'a') is True  # single letters are easy
        assert contains('abc', 'b') is True
        assert contains('abc', 'c') is True
        assert contains('abc', 'ab') is True  # multiple letters are harder
        assert contains('abc', 'bc') is True
        assert contains('abc', 'abc') is True  # all strings contain themselves
        assert contains('aaa', 'a') is True  # multiple occurrences
        assert contains('aaa', 'aa') is True  # overlapping pattern
        # TODO: Write more positive test cases with assert is True statements
        # ...

    def test_contains_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert contains('abc', 'z') is False  # remember to test other letters
        assert contains('abc', 'ac') is False  # important to test close cases
        assert contains('abc', 'az') is False  # first letter, but not last
        assert contains('abc', 'abz') is False  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is False statements
        # ...

    def test_contains_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert contains('ababc', 'ab') is True  # multiple occurrences
        assert contains('banana', 'na') is True  # multiple occurrences
        assert contains('ababc', 'abc') is True  # overlapping prefix
        assert contains('bananas', 'nas') is True  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        # ...

    def test_find_index_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_index('abc', '') == 0  # all strings contain empty string
        assert find_index('abc', 'a') == 0  # single letters are easy
        assert find_index('abc', 'b') == 1
        assert find_index('abc', 'c') == 2
        assert find_index('abc', 'ab') == 0  # multiple letters are harder
        assert find_index('abc', 'bc') == 1
        assert find_index('abc', 'abc') == 0  # all strings contain themselves
        assert find_index('aaa', 'a') == 0  # multiple occurrences
        assert find_index('aaa', 'aa') == 0  # overlapping pattern
        assert find_index("aaaaab", "aaab") == 2
        # TODO: Write more positive test cases with assert equal int statements
        # ...

    def test_find_index_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_index('abc', 'z') is None  # remember to test other letters
        assert find_index('abc', 'ac') is None  # important to test close cases
        assert find_index('abc', 'az') is None  # first letter, but not last
        assert find_index('abc', 'abz') is None  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert is None statements
        # ...

    def test_find_index_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_index('ababc', 'abc') == 2  # overlapping prefix
        assert find_index('bananas', 'nas') == 4  # overlapping prefix
        assert find_index('abcabcabc', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcab', 'abc') == 0  # multiple occurrences
        assert find_index('abcabcdef', 'abcd') == 3  # overlapping prefix
        assert find_index('abcabcdef', 'abcdef') == 3  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcde') == 7  # overlapping prefix
        assert find_index('abcabcdabcde', 'abcd') == 3  # multiple occurrences, overlapping prefix
        assert find_index('abra cadabra', 'abra') == 0  # multiple occurrences
        assert find_index('abra cadabra', 'adab') == 6  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        # ...

    def test_find_all_indices_with_matching_patterns(self):
        # Positive test cases (examples) with matching patterns
        assert find_all_indices('abc', '') == [0, 1, 2]  # all strings contain empty string
        assert find_all_indices('abc', 'a') == [0]  # single letters are easy
        assert find_all_indices('abc', 'b') == [1]
        assert find_all_indices('abc', 'c') == [2]
        assert find_all_indices('abc', 'ab') == [0]  # multiple letters are harder
        assert find_all_indices('abc', 'bc') == [1]
        assert find_all_indices('abc', 'abc') == [0]  # all strings contain themselves
        assert find_all_indices('aaa', 'a') == [0, 1, 2]  # multiple occurrences
        assert find_all_indices('aaa', 'aa') == [0, 1]  # overlapping pattern
        # TODO: Write more positive test cases with assert equal list statements
        # ...

    def test_find_all_indices_with_non_matching_patterns(self):
        # Negative test cases (counterexamples) with non-matching patterns
        assert find_all_indices('abc', 'z') == []  # remember to test other letters
        assert find_all_indices('abc', 'ac') == []  # important to test close cases
        assert find_all_indices('abc', 'az') == []  # first letter, but not last
        assert find_all_indices('abc', 'abz') == []  # first 2 letters, but not last
        # TODO: Write more negative test cases with assert equal list statements
        # ...

    def test_find_all_indices_with_complex_patterns(self):
        # Difficult test cases (examples) with complex patterns
        assert find_all_indices('ababc', 'abc') == [2]  # overlapping prefix
        assert find_all_indices('bananas', 'nas') == [4]  # overlapping prefix
        assert find_all_indices('abcabcabc', 'abc') == [0, 3, 6]  # multiple occurrences
        assert find_all_indices('abcabcab', 'abc') == [0, 3]  # multiple occurrences
        assert find_all_indices('abcabcdef', 'abcd') == [3]  # overlapping prefix
        assert find_all_indices('abcabcdef', 'abcdef') == [3]  # overlapping prefix
        assert find_all_indices('abcabcdabcde', 'abcde') == [7]  # overlapping prefix
        assert find_all_indices('abcabcdabcde', 'abcd') == [3, 7]  # multiple occurrences, overlapping prefix
        assert find_all_indices('abra cadabra', 'abra') == [0, 8]  # multiple occurrences
        assert find_all_indices('abra cadabra', 'adab') == [6]  # overlapping prefix
        # TODO: Write more test cases that check complex patterns or edge cases
        # You'll need a lot more than this to test your algorithm's robustness
        # ...


if __name__ == '__main__':
    unittest.main()
