# coding:utf-8
import sys
sys.path.append('../')

from util import print_list_node, general_list_node


def merge_two_lists(l1, l2):
    if not l1 or not l2:
        return l1 if l1 else l2
    head = pcursor = qcursor = None
    if l1.val > l2.val:
        head = l2
        qcursor = l1
    else:
        head = l1
        qcursor = l2
    pcursor = head.next
    cursor = head
    while pcursor and qcursor:
        if pcursor.val > qcursor.val:
            cursor.next = qcursor
            qcursor = qcursor.next
        else:
            cursor.next = pcursor
            pcursor = pcursor.next
        cursor = cursor.next
    cursor.next = pcursor if pcursor else qcursor
    return head
L2 = general_list_node((vals))
L1 = general_list_node((1, 2, 4))
NL = merge_two_lists(L1, L2)
print_list_node(NL)


