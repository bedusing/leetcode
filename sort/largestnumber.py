# coding:utf-8
"""
Given a list of non negative integers, arrange them such that they form the largest number.
For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
Note: The result may be very large, so you need to return a string instead of an integer.
"""


def _get_number_digits(number):
    if 0 == number:
        return [0]
    number_digits = []
    while number:
        number_digits.insert(0, number % 10)
        number = number / 10
    return number_digits


def _cmp3(a, b):
    a_digits = _get_number_digits(a)
    b_digits = _get_number_digits(b)
    a_temp_digits = []
    a_temp_digits.extend(a_digits)
    a_digits.extend(b_digits)
    b_digits.extend(a_temp_digits)
    for index in xrange(len(a_digits)):
        if a_digits[index] > b_digits[index]:
            return 1
        if a_digits[index] < b_digits[index]:
            return -1
    return 0

def _cmp2(a, b):
    """
    maybe overflow
    """
    a_digits = _get_number_digits(a)
    b_digits = _get_number_digits(b)
    a_count = len(a_digits)
    b_count = len(b_digits)
    temp_a = a * (10 ** b_count) + b
    temp_b = b * (10 ** a_count) + a
    return 1 if temp_a > temp_b else -1


def _cmp(a, b):
    if a == b:
        return 0
    a_digits = _get_number_digits(a)
    b_digits = _get_number_digits(b)
    a_count = len(a_digits)
    b_count = len(b_digits)
    count = a_count + b_count
    index = 1
    for index in xrange(1, count + 1):
        a_digit = a_digits[-
                           index] if index <= a_count else b_digits[a_count - index]
        b_digit = b_digits[-
                           index] if index <= b_count else a_digits[b_count - index]
        if a_digit > b_digit:
            return 1
        if b_digit > a_digit:
            return -1
    return 0


def get_largest_number(number_list):
    all_zero_flag = True
    for number in number_list:
        if not 0 == number:
            all_zero_flag = False
            break
    if all_zero_flag:
        return '0'
    number_list.sort(cmp=_cmp3, reverse=True)
    digits = [str(number) for number in number_list]
    return "".join(digits)

print get_largest_number([3, 30, 34, 5, 9])
print get_largest_number([0, 0])
print get_largest_number([121, 12])
print get_largest_number([830, 8308])
print get_largest_number([20, 1])
