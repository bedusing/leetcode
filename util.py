# coding:utf-8


class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None


def general_list_node(vals):
    head = None
    pcursor = None
    for val in vals:
        if not head:
            head = pcursor = ListNode(val)
        else:
            pcursor.next = ListNode(val)
            pcursor = pcursor.next
    return head


def general_circle_list_node(vals,connect_index):
    head = None
    pcursor = None
    start_node = None
    index = 0
    for val in vals:
        if not head:
            head = pcursor = ListNode(val)
        else:
            pcursor.next = ListNode(val)
            pcursor = pcursor.next
        if index == connect_index:
            start_node = pcursor
        index += 1
    if pcursor:
        pcursor.next = start_node
    return head


def print_list_node(head):
    vals = []
    pcursor = head
    while pcursor:
        vals.append(str(pcursor.val))
        pcursor = pcursor.next
    print '->'.join(vals)
