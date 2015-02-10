# coding:utf-8

"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].
"""


def delete_duplicates(array):
    count = len(array)
    index = count - 1
    prefix_index = index - 1
    while prefix_index >= 0:
        if array[index] == array[prefix_index]:
            del array[index]
            index = prefix_index
            prefix_index -= 1
        else:
            index = prefix_index
            prefix_index -= 1
    return array

print delete_duplicates([12, 12, 13, 23, 23])
print delete_duplicates([12, 12])
print delete_duplicates([])
