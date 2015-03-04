# coding:utf-8


def the_longest_incr_sub_seq(seq):
    """
    给定一个数列，长度为N，
    求这个数列的最长上升（递增）子数列（LIS）的长度.
    以 1 7 2 8 3 4 为例
    这个数列的最长递增子数列是 1 2 3 4，长度为4；
    次长的长度为3， 包括 1 7 8; 1 2 3 等.

    问题定义：
    设F{k}为：以数列中第k项结尾的最长递增子序列的长度.
    求F{1}..F{N} 中的最大值.
    转移方程：
    F{1} = 1 （根据状态定义导出边界情况）
    F{k} = max(F{i}+1 | A{k}>A{i}, when i in (1..k-1)) (k>1)
    """
    def _get_k_len(seq, index, max_len_seq):
        if 0 == index:
            return 1
        max_len = 0
        for i in xrange(index):
            klen = max_len_seq[i] if i in max_len_seq else _get_k_len(seq, i, max_len_seq)
            if seq[index] > seq[i]:
                klen += 1
            max_len = max(klen, max_len)
        return max_len
    count = len(seq)
    max_len = 0
    max_len_seq = {}   
    for index in xrange(count):
        klen = max_len_seq[index] = _get_k_len(seq, index, max_len_seq)
        max_len = max(max_len, klen)
    return max_len

print the_longest_incr_sub_seq([1, 7, 2, 8, 3, 4])
  