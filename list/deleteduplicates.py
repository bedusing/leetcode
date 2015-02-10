# coding:utf-8


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

def delete_duplicates(head):
    if not head:
        return head
    p = head
    q = head.next
    while p and q:
        if p.val == q.val:
            p.next = q.next
            q = p.next
        else:
            p = q
            q = q.next
    return head


def general_list_node(vals):
    head = None
    p = None
    for val in vals:
        if not head:
            head = p = ListNode(val)
        else:
            p.next = ListNode(val)
            p = p.next
    return head


def print_list_node(head):
    vals = []
    p = head
    while p:
        vals.append(str(p.val))
        p = p.next
    print '->'.join(vals)

def test(vals):
    HEAD = general_list_node(vals)
    print "list:"
    print_list_node(HEAD)
    HEAD = delete_duplicates(HEAD)
    print "after delete:"
    print_list_node(HEAD)

test((12, 12, 13, 14, 14))
test((12,12))
test((12,))
test(())