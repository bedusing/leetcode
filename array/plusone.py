# coding:utf-8
"""
Given a non-negative number represented as an array of digits, plus one to the number.
The digits are stored such that the most significant digit is at the head of the list.
"""


def plus_one(digits):
    index = len(digits) - 1
    step = 0
    digit = 1
    while index >= 0:
        val = digits[index] + digit + step
        digits[index] = val % 10
        step = val / 10
        digit = 0
        if not step:
            break
        index -= 1
    if step:
        digits.insert(0, 1)
    return digits

print plus_one([9, 9, 9, 9])
print plus_one([0])
