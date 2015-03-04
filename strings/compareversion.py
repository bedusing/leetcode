# coding:utf-8
"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:
"""


def campare_versions(version1, version2):
    ver1_list = version1.split('.')
    ver2_list = version2.split('.')
    def _camp(ver1, ver2):
        if ver1 > ver2:
            return 1
        elif ver2 > ver1:
            return -1
        else:
            return 0
    ver1_len = len(ver1_list)
    ver2_len = len(ver2_list)
    count = max(ver1_len, ver2_len)
    index = 0
    while index < count:
        ver1 = int(ver1_list[index]) if index < ver1_len else 0
        ver2 = int(ver2_list[index]) if index < ver2_len else 0
        flag = _camp(ver1, ver2)
        if 0 != flag:
            return flag
        index += 1
    return 0

print campare_versions('1.2', '1.3')