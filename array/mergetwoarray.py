# coding:utf-8
"""
Given two sorted integer arrays A and B, merge B into A as one sorted array.
Note:
You may assume that A has enough space (size that is greater or equal to m + n) to
hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
"""


def merge(A, m, B, n):
    aindex = 0
    while aindex < m:
        A[m + n - 1 - aindex] = A[m - 1 - aindex]
        aindex += 1
    aindex = 0
    bindex = 0
    index = 0
    while index < m + n:
        if bindex >= n:
            break
        if aindex < m and A[n + aindex] < B[bindex]:
            A[index] = A[n + aindex]
            aindex += 1
        else:
            A[index] = B[bindex]
            bindex += 1
        index += 1


A = [1, 2, 4, 5, 6, 0]
B = [3]
merge(A, 5, B, 1)
print A
