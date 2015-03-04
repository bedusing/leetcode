# coding:utf-8

"""
A peak element is an element that is greater than its neighbors.
Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that num[-1] = num[n] = -∞.
For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.
click to show spoilers.
Note:
Your solution should be in logarithmic complexity.
"""


def find_peak_element(ary):
    index = 0
    count = len(ary)
    while index < count:
        if index - 1 < 0 or ary[index] > ary[index - 1]:
            if index + 1 >= count or ary[index] > ary[index + 1]:
                return index
        if ary[index] > ary[index + 1]:
            index += 2
        else:
            index += 1

print find_peak_element([1, 2, 3, 4])
