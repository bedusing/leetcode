# coding:utf-8


def find_the_min(number_list):
    """
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    Find the minimum element.
    You may assume no duplicate exists in the array.
    """
    pre_index = 0
    count = len(number_list)
    for index in xrange(0, count):
        if number_list[pre_index] > number_list[index]:
            return number_list[index]
        pre_index = index
    return number_list[0]


def find_the_min2(number_list):
    """
    Suppose a sorted array is rotated at some pivot unknown to you beforehand.
    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
    Find the minimum element.
    You may assume no duplicate exists in the array.
    """
    def _find_the_min(start, end):
        if start == end:
            return number_list[start]
        median = (start + end) / 2
        if number_list[median] < number_list[median - 1]:
            return number_list[median]
        elif number_list[median] > number_list[end]:
            return _find_the_min(median + 1, end)
        else:
            return _find_the_min(start, median)
    return _find_the_min(0, len(number_list) - 1)

print find_the_min2([1, 2])
