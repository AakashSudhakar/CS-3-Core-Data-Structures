#!python
# NAME: bases.py
# CONTRIBUTOR: Aakash Sudhakar

# ================================== GLOBAL IMPORT STATEMENTS ====================================
# TODO: Wrap all in class and update unit tests

import sys, string

# ================== METHOD TO DECODE GIVEN BASE-CONVERTED NUMBER INTO BASE 10 ===================
# TODO: Try recursive solution
def decode(digits, base):
    # Handle up to base 36 [0-9a-z]
    assert (2 <= base <= 36), "\nBASE IS OUT-OF-RANGE: {}\n".format(base)

    # Creates dictionary of possible base conversion digits
    base_conversion_dict, iterator, base_sum = dict(), 0, 0
    for item in (string.digits + string.ascii_lowercase):
        base_conversion_dict[item] = iterator
        iterator += 1

    # Iterates through digit string and converts into base power sum in base 10
    for index, digit in enumerate(str(digits)[::-1]):
        base_sum += int(base_conversion_dict[digit]) * (base ** index)
    return base_sum
    
    # return sum([(int(base_conversion_dict[digit]) * (base ** index)) for index, digit in enumerate(str(digits)[::-1])])


# ==================== METHOD TO ENCODE BASE 10 NUMBER INTO BASE-CONVERSION ======================
# TODO: Try iterative solution
def encode(number, base):
    # Handle up to base 36 [0-9a-z] and unsigned numbers only for now
    assert (2 <= base <= 36), "\nBASE IS OUT OF RANGE: {}\n".format(base)
    assert number >= 0, "\nNUMBER IS NEGATIVE: {}\n".format(number)

    base_list = string.digits + string.ascii_lowercase
    if number < base:
        return base_list[number]
    else:
        return encode(number // base, base) + base_list[number % base]


# =================== METHOD TO CONVERT ONE BASE-CONVERTED NUMBER TO ANOTHER =====================
def convert(digits, base_original, base_final):
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base_original <= 36, "\nORIGINAL BASE IS OUT OF RANGE: {}\n".format(base_original)
    assert 2 <= base_final <= 36, "\nFINAL BASE IS OUT OF RANGE: {}\n".format(base_final)

    return encode(decode(digits, base_original), base_final)


# ======================= METHOD TO TEST SIMPLE CASES OF DECODE() METHOD =========================
def test_decode():
    # Testing decode()
    args = sys.argv[1:]                                         # Ignore script file name
    if len(args) == 2:
        digits = args[0].lower()
        base = int(args[1])
        result = decode(digits, base)
        print("\n{} IN BASE {} IS {} IN BASE 10\n".format(digits, base, result))
    else:
        print("\nUSAGE: {} [digits] [base]".format(sys.argv[0]))
        print("DECODES [digits] FROM [base] TO BASE 10\n")

# ======================= METHOD TO TEST SIMPLE CASES OF ENCODE() METHOD =========================
def test_encode():
    # Testing encode()
    args = sys.argv[1:]   
    if len(args) == 2:                                      # Ignore script file name
        digits, base = int(args[0]), int(args[1])
        result = encode(digits, base)
        print("\n{} IN BASE 10 IS {} IN BASE {}\n".format(digits, result.upper(), base))
    else:
        print("\nUSAGE: {} [digits] [base]".format(sys.argv[0]))
        print("ENCODES [digits] FROM BASE 10 TO [base]\n")
        

# ======================= METHOD TO TEST SIMPLE CASES OF CONVERT() METHOD ========================
def test_convert():
    # Testing convert()
    args = sys.argv[1:]
    if len(args) == 3:
        digits = args[0]
        base_original = int(args[1])
        base_final = int(args[2])
        result = convert(digits, base_original, base_final)         # Convert given digits between bases
        print("\n{} IN BASE {} IS {} IN BASE {}\n".format(digits, base_original, result.upper(), base_final))
    else:
        print("\nUSAGE: {} [digits] [base_original] [base_final]".format(sys.argv[0]))
        print("CONVERTS [digits] FROM [base_original] TO [base_final]\n")

# ====================================== MAIN RUN FUNCTION =======================================
def main():
    # test_decode()
    # test_encode()
    test_convert()


if __name__ == "__main__":
    main()
