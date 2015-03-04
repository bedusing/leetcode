# coding:utf-8

"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
"""


def delete_duplicates(ary):
    count = len(ary)
    if 0 == count:
        return 0
    index = 1
    prefix_index = 0
    while index < count:
        if ary[prefix_index] != ary[index]:
            prefix_index += 1
            ary[prefix_index] = ary[index]
        index += 1
    return prefix_index + 1

print delete_duplicates([12, 12, 13, 23, 23])
print delete_duplicates([12, 12])
print delete_duplicates([])
