# coding:utf-8
"""
Write a function to find the longest common prefix string amongst an array of strings.
"""


def longest_common_prefix(strs):
    str_prefix = ''
    if not strs:
        return str_prefix
    if 1 == len(strs):
        return strs[0]
    max_index = 1
    flag = False
    while 1:
        if len(strs[0]) < max_index:
            break
        temp_prefix = strs[0][:max_index]
        for _str in strs:
            if not temp_prefix == _str[:max_index]:
                flag = True
                break
        if flag:
            break
        str_prefix = strs[0][:max_index]
        max_index += 1
    return str_prefix

STRS = ("zhonglibo", "zhongliwen", "zhongdongjiang", "zhonglinzhi")
print "result:", longest_common_prefix(STRS)

