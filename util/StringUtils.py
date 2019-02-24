def is_valid_binary_string(binary_string='', bit_number=-1):
    if 0 < bit_number != len(binary_string):
        return False
    for c in binary_string:
        if not (c == '0' or c == '1'):
            return False
    return True


def binary_to_integer(binary):
    binary = str(binary)

    value = 0
    pot = 1
    for x in range(len(binary) - 1, -1, -1):
        if binary[x] == '1':
            value += pot
        pot *= 2
    return value


def is_every_digit_even(value):
    value = str(value)
    if value.isdigit():
        for c in value:
            if int(c) % 2 != 0:
                return False
        return True
    else:
        return False


def count_digits(value):
    count = 0
    for c in value:
        if c.isdigit():
            count += 1
    return count


def count_letters(value):
    count = 0
    for c in value:
        if c.isalpha():
            count += 1
    return count


def count_upper(value):
    count = 0
    for c in value:
        if c.isupper():
            count += 1
    return count


def count_lower(value):
    count = 0
    for c in value:
        if c.islower():
            count += 1
    return count
