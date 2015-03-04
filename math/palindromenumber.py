# coding:utf-8
"""
Determine whether an integer is a palindrome. Do this without enumbertra space.
click to show spoilers.

Some hints:
Could negative integers be palindromes? (ie, -1)
If you are thinking of converting the integer to string, note the restriction of using extra space.
You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", 
you know that the reversed integer might overflow. How would you handle such case?
There is a more generic way of solving this problem.
"""


def is_palindrome_number(number):
    if number < 0:
        return False
    digit_cnt = 1
    while number / (10 ** digit_cnt):
        digit_cnt += 1
    index = 1
    while index <= digit_cnt / 2:
        front_digit = number / (10 ** (digit_cnt - index)) % 10
        back_digit = (number - number / (10 ** index) * (10 ** index)) / \
            10 ** (index - 1)
        if front_digit != back_digit:
            return False
        index += 1
    return True

print is_palindrome_number(12321) 
