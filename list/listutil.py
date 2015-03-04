# coding:utf-8
import sys
sys.path.append('../')

from util import print_list_node, general_circle_list_node, general_list_node, RandomListNode


def insertion_two_list(head_a, head_b):
    """
    Write a program to find the node at which the intersection of two singly linked lists begins.
    For example, the following two linked lists:

    A:          a1 → a2
                       ↘
                         c1 → c2 → c3
                       ↗            
    B:     b1 → b2 → b3
    begin to intersect at node c1.
    Notes:
    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.
    """
    def get_list_node_count(head):
        pnode = head
        count = 0
        while pnode:
            count += 1
            pnode = pnode.next
        return count
    head_a_count = get_list_node_count(head_a)
    head_b_count = get_list_node_count(head_b)
    diff_count = abs(head_a_count - head_b_count)
    pstep = head_a
    qstep = head_b
    index = 0
    if head_a_count > head_b_count:
        while index < diff_count:
            pstep = pstep.next
            index += 1
    elif head_a_count < head_b_count:
        while index < diff_count:
            qstep = qstep.next
            index += 1
    head = None
    while pstep and qstep:
        if pstep.val == qstep.val:
            if not head:
                head = pstep
        else:
            head = None
        pstep = pstep.next
        qstep = qstep.next

    return head


def test_insertion_two_list():
    HEADA = general_list_node([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21])
    HEADB = general_list_node([17, 19, 21])
    print insertion_two_list(HEADA, HEADB)


def is_circle_list(head):
    """
    Given a linked list, determine if it has a cycle in it.
    Follow up:
    Can you solve it without using extra space?
    """
    pstep = qstep = head
    while pstep and qstep and qstep.next:
        pstep = pstep.next
        qstep = qstep.next.next
        if pstep == qstep:
            return True
    return False


def is_circle_list2(head):
    """
    Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
    Follow up:
    Can you solve it without using extra space?
    """
    pstep = qstep = head
    flag = False
    while pstep and qstep and qstep.next:
        pstep = pstep.next
        qstep = qstep.next.next
        if pstep == qstep:
            flag = True
            break
    if not flag:
        return None

    def get_node_count(qstep):
        circle_node_count = 0
        while qstep:
            circle_node_count += 1
            if pstep == qstep:
                break
            qstep = qstep.next
        return circle_node_count
    qstep = qstep.next
    node_count_from_cursor = get_node_count(qstep)
    qstep = head
    node_count_from_head = get_node_count(qstep)
    step_count = abs(node_count_from_cursor - node_count_from_head)
    if 0 == step_count:
        return head
    pstep = pstep.next
    qstep = head
    index = 0
    if node_count_from_cursor > node_count_from_head:
        while index < step_count:
            pstep = pstep.next
            index += 1
    else:
        while index < step_count:
            qstep = qstep.next
            index += 1
    while 1:
        if pstep == qstep:
            return pstep
        pstep = pstep.next
        qstep = qstep.next


def test_is_circle_list():
    CHEAD = general_circle_list_node([12, 32, 11, 23], 3)
    print "circle start node", is_circle_list2(CHEAD).val


def swap_pairs(head):
    """
    Given a linked list, swap every two adjacent nodes and return its head.
    For example,
    Given 1->2->3->4, you should return the list as 2->1->4->3.
    Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
    """
    # @param a ListNode
    # @return a ListNode
    if not head:
        return head
    pstep = head
    qstep = head.next
    cursor_step = None
    new_head = None
    while pstep and qstep:
        pstep.next = qstep.next
        qstep.next = pstep
        if not new_head:
            new_head = qstep
        else:
            cursor_step.next = qstep
        cursor_step = pstep
        pstep = pstep.next
        qstep = pstep.next if pstep else None
    return new_head if new_head else head


def test_swap_pairs():
    def test(vals):
        head = general_list_node(vals)
        print_list_node(head)
        new_head = swap_pairs(head)
        print_list_node(new_head)
    test([12, 33, 44, 32, 123, 31, 55])
    test([1])
    test([])

# test_swap_pairs()


def insertion_sort_list(head):
    """
    Sort a linked list using insertion sort
    note: int judge much faster than pointer
    @return a ListNode
    """
    if not head:
        return None
    sort_count = 0
    last_cursor = head
    qstep = head.next
    last_cursor.next = None
    head.next = None
    while qstep:
        qcursor = qstep
        qstep = qstep.next
        sort_count += 1
        if last_cursor.val <= qcursor.val:
            last_cursor.next = qcursor
            last_cursor = qcursor
            last_cursor.next = None
            continue
        pstep = head
        pcursor_step = None
        index = 0
        while index < sort_count:
            if qcursor.val < pstep.val:
                qcursor.next = pstep
                if pstep == head:
                    head = qcursor
                if pcursor_step:
                    pcursor_step.next = qcursor
                break
            pcursor_step = pstep
            pstep = pstep.next
            index += 1
    return head


def test_insertion_sort_list():
    def test(vals):
        head = general_list_node(vals)
        print_list_node(head)
        new_head = insertion_sort_list(head)
        print_list_node(new_head)
    test([33, 44, 32, 123, 31, 55])
    test([1])
    test([])

# test_insertion_sort_list()


def quick_sort_list(head):

    def quick_sort(begin, end):
        if begin != end:
            median = get_position(begin, end)
            quick_sort(begin, median)
            quick_sort(median.next, end)

    def get_position(begin, end):
        pstep = begin
        qstep = begin.next
        key = begin.val
        while qstep != end:
            if qstep.val < key:
                pstep = pstep.next
                pstep.val, qstep.val = qstep.val, pstep.val
            qstep = qstep.next
        begin.val, pstep.val = pstep.val, begin.val
        return pstep
    if not head:
        return head
    begin = end = head
    while end.next:
        end = end.next
    quick_sort(begin, None)
    return head


def test_quick_sort_list():
    def test(vals):
        head = general_list_node(vals)
        print_list_node(head)
        new_head = quick_sort_list(head)
        print_list_node(new_head)
    test([33, 44, 32, 123, 31, 55])
    test([1])
    test([])

# test_quick_sort_list()


def delete_duplicates(head):
    if not head:
        return None
    pstep = head
    qstep = head.next
    key = qstep.val
    new_head = None
    while qstep:
        if pstep.val != qstep.val:
            if key == pstep.val:
                if not new_head:
                    tstep = new_head = pstep
                else:
                    tstep.next = pstep
                    tstep = pstep
        key = qstep.val
        pstep = pstep.next
        qstep = qstep.next
    return new_head


def delete_duplicates2(head):
    if not head or not head.next:
        return head
    fstep = None
    mstep = head
    lstep = head.next
    new_head = None
    tstep = None
    while mstep:
        nstep = mstep.next
        mstep.next = None
        if not fstep or fstep.val != mstep.val:
            if not lstep or lstep.val != mstep.val:
                if not new_head:
                    tstep = new_head = mstep
                else:
                    tstep.next = mstep
                    tstep = mstep
        fstep = mstep
        mstep = nstep
        lstep = mstep.next if mstep else None
    return new_head


def test_delete_duplicates():
    def test(vals):
        head = general_list_node(vals)
        print_list_node(head)
        new_head = delete_duplicates2(head)
        print_list_node(new_head)
    test([33, 33, 32, 32, 1, 2, 31, 31, 55])
    test([1, 2])
    test([1])
    test([1, 2, 2])
    test([])

# test_delete_duplicates()


def rotate_list(head, k):
    """
    Given a list, rotate the list to the right by k places, where k is non-negative.
    For example:
    Given 1->2->3->4->5->NULL and k = 2,
    return 4->5->1->2->3->NULL.
    note: 
    """
    if not head:
        return head
    pstep = head
    llen = 0
    while pstep.next:
        pstep = pstep.next
        llen += 1
    llen += 1
    k = k % llen
    if k == 0:
        return head
    index = 1
    pstep.next = head
    pstep = head
    while index < llen - k:
        pstep = pstep.next
        index += 1
    head = pstep.next
    pstep.next = None
    return head


def test_rotate_list():
    def test(vals):
        head = general_list_node(vals)
        print_list_node(head)
        new_head = rotate_list(head, 4)
        print_list_node(new_head)
    test([33, 33, 32, 32, 1, 2, 31, 31, 55])
    test([1, 2])
    test([1])
    test([1, 2, 3])
    test([])

# test_rotate_list()


def record_list(head):
    """
    Given a singly linked list L: L0→L1→…→Ln-1→Ln,
    reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
    You must do this in-place without altering the nodes' values.
    For example,
    Given {1,2,3,4}, reorder it to {1,4,2,3}.
    """
    pstep = head
    llen = 0
    while pstep:
        llen += 1
        pstep = pstep.next
    if llen < 3:
        return
    index = 0
    pstep = head
    median = llen / 2
    median_head = None
    while pstep:
        if index < median:
            pstep = pstep.next
        elif index == median:
            tstep = pstep.next
            pstep.next = None
            pstep = tstep
        else:
            tstep = pstep.next
            pstep.next = median_head
            median_head = pstep
            pstep = tstep
        index += 1
    pstep = head
    qstep = median_head
    while qstep:
        t_pstep = pstep.next
        t_qstep = qstep.next
        pstep.next = qstep
        qstep.next = t_pstep
        pstep = t_pstep
        qstep = t_qstep


def test_record_list():
    def test(vals):
        head = general_list_node(vals)
        print_list_node(head)
        record_list(head)
        print_list_node(head)
    test([33, 23, 12, 322, 1, 2, 311, 131, 55])
    test([1, 2, 3, 4])
    test([1])
    test([1, 2, 3])
    test([])

# test_record_list()


def partition_list(head, x):
    """
    Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
    You should preserve the original relative order of the nodes in each of the two partitions.
    For example,
    Given 1->4->3->2->5->2 and x = 3,
    return 1->2->2->4->3->5.
    """
    less_head = less_step = None
    large_head = large_step = None
    pstep = head
    while pstep:
        tstep = pstep
        pstep = pstep.next
        tstep.next = None
        if tstep.val < x:
            if not less_head:
                less_head = less_step = tstep
            else:
                less_step.next = tstep
                less_step = tstep
        else:
            if not large_head:
                large_head = large_step = tstep
            else:
                large_step.next = tstep
                large_step = tstep
    if less_step:
        less_step.next = large_head
    return less_head if less_head else large_head


def test_partition_list():
    def test(vals):
        head = general_list_node(vals)
        print_list_node(head)
        head = partition_list(head, 33)
        print_list_node(head)

    test([44, 33, 23, 12])
    test([1, 2, 3, 4])
    test([44, 33, 34, 54])

# test_partition_list()


def merge_k_sort_list(head_list):
    """
    Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
    """
    for head in head_list:
        pass


def reverse_list(head, start, end):
    """
    Reverse a linked list from position m to n. Do it in-place and in one-pass.
    For example:
    Given 1->2->3->4->5->NULL, m = 2 and n = 4,
    return 1->4->3->2->5->NULL.
    Note:
    Given m, n satisfy the following condition:
    1 ≤ m ≤ n ≤ length of list.
    """
    if start == end:
        return head
    index = 0
    pstep = head
    main_start_node = None
    sub_end_node = None
    sub_pstart = None
    while pstep:
        index += 1
        if index < start:
            main_start_node = pstep
            pstep = pstep.next
        elif start == index:
            sub_end_node = sub_pstart = pstep
            pstep = pstep.next
        elif index < end:
            tstep = pstep.next
            pstep.next = sub_pstart
            sub_pstart = pstep
            pstep = tstep
        else:
            sub_end_node.next = pstep.next
            pstep.next = sub_pstart
            if main_start_node:
                main_start_node.next = pstep
                return head
            return pstep


def test_reverse_list():
    def test(vals, start, end):
        head = general_list_node(vals)
        print_list_node(head)
        head = reverse_list(head, start, end)
        print_list_node(head)
    test([33, 23, 12, 322, 1, 2, 311, 131, 55], 3, 5)
    test([1, 2, 3, 4], 1, 4)

# test_reverse_list()


def _reverse_list(head):
    if not head:
        return head
    pstep = head
    qstep = head.next
    pstep.next = None
    while qstep:
        tstep = qstep.next
        qstep.next = pstep
        pstep = qstep
        qstep = tstep
    return pstep


def _test_reverse_list():
    def test(vals):
        head = general_list_node(vals)
        print_list_node(head)
        head = _reverse_list(head)
        print_list_node(head)
    test([33, 23, 12, 322, 1, 2, 311, 131, 55])
    test([1, 2, 3, 4])
    test([])

_test_reverse_list()


def reverse_k_group(head, k):
    """
    Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
    If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
    You may not alter the values in the nodes, only nodes itself may be changed.
    Only constant memory is allowed.
    For example,
    Given this linked list: 1->2->3->4->5
    For k = 2, you should return: 2->1->4->3->5
    For k = 3, you should return: 3->2->1->4->5
    """
    pstep = head
    llen = 0
    while pstep:
        pstep = pstep.next
        llen += 1
    if k > llen or k < 2:
        return head
    pstep = head
    index = 0
    sub_head = head
    master_head = sub_tail = None
    while pstep:
        index += 1
        if index % k == 0:
            tstep = pstep
            pstep = pstep.next
            tstep.next = None

            sub_list = _reverse_list(sub_head)
            if not master_head:
                master_head = sub_list
            else:
                sub_tail.next = sub_list
            sub_tail = sub_head
            sub_tail.next = pstep
            sub_head = pstep
        else:
            pstep = pstep.next
    return master_head


def reverse_k_group2(head, k):
    pstep = head
    llen = 0
    while pstep:
        pstep = pstep.next
        llen += 1
    if k > llen or k < 2:
        return head
    kgroup = llen / k
    for group in xrange(kgroup):
        head = reverse_list(head, k * group + 1, k * (group + 1))
    return head


def test_reverse_k_group_list():
    def test(vals, k):
        head = general_list_node(vals)
        print_list_node(head)
        head = reverse_k_group(head, k)
        print_list_node(head)
    test([33, 23, 12, 322, 1, 2, 311, 131, 55], 6)
    test([1, 2], 2)

# test_reverse_k_group_list()


def copy_random_list(head):
    """
    A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
    Return a deep copy of the list.
    """
    pstep = qstep = head
    new_nodes = {}
    while pstep:
        new_nodes[pstep] = RandomListNode(pstep.label)
        pstep = pstep.next
    while qstep:
        new_node = new_nodes[qstep]
        new_node.next = new_nodes.get(qstep.next, None)
        new_node.random = new_nodes.get(qstep.random, None)
        qstep = qstep.next
    return new_nodes.get(head, None)


def copy_random_list2(head):
    def create_new_node(node):
        if not node:
            return None
        new_node = new_nodes.get(node)
        if not new_node:
            new_node = new_nodes[node] = RandomListNode(pstep.label)
        return new_node
    pstep = head
    new_nodes = {}
    while pstep:
        new_node = create_new_node(pstep)
        new_node.next = create_new_node(pstep.next)
        new_node.random = create_new_node(pstep.random)
        pstep = pstep.next
    return new_nodes.get(head, None)
