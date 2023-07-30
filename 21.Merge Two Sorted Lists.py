'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    v = []
    while list1 is not None:
        v.append(list1.val)
        list1 = list1.next

    while list2 is not None:
        v.append(list2.val)
        list2 = list2.next

    v = sorted(v)

    cur = dummy = ListNode()
    for e in v:
        cur.next = ListNode(e)
        cur = cur.next
    # print(dummy.next)
    return dummy.next




