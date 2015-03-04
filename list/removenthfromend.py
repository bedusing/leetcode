# coding:utf-8
"""
Given a linked list, remove the nth node from the end of list and return its head.
For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""
import sys
sys.path.append('../')
from util import general_list_node, print_list_node


def remove_nth_from_front(head, n):
    if 1 == n:
        head = head.next
        return head
    pcursor = head
    index = 0
    while pcursor:
        index += 1
        if n - 1 == index:
            pcursor.next = pcursor.next.next if pcursor.next else None 
            break
        pcursor = pcursor.next
    return head


def remove_nth_from_end(head, n):
    """
    len = m + n, just move (len - n)steps start from front 
    """
    tag_ptr = head
    ptr = head
    counter = 0
    while ptr:
        if counter > n:
            tag_ptr = tag_ptr.next
        ptr = ptr.next
        counter += 1
    if counter > n:
        tag_ptr.next = tag_ptr.next.next
        return head
    if counter == n:
        return head.next
    return head

HEAD = general_list_node((1, 2, 3, 4))
print_list_node(HEAD)
HEAD = remove_nth_from_front(HEAD, -1)
print_list_node(HEAD)

 