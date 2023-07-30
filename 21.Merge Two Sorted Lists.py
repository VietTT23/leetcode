'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
'''

'''
link: 
https://pythontutor.com/render.html#code=class%20ListNode%3A%0A%20%20%20%20def%20__init__%28self,%20x%29%3A%0A%20%20%20%20%20%20%20%20self.val%20%3D%20x%0A%20%20%20%20%20%20%20%20self.next%20%3D%20None%0A%0A%0Adef%20lst2link%28lst%29%3A%0A%20%20%20%20cur%20%3D%20dummy%20%3D%20ListNode%280%29%0A%20%20%20%20for%20e%20in%20lst%3A%0A%20%20%20%20%20%20%20%20cur.next%20%3D%20ListNode%28e%29%0A%20%20%20%20%20%20%20%20cur%20%3D%20cur.next%0A%20%20%20%20return%20dummy.next%0A%0A_list1%20%3D%20%5B1,2,3,4%5D%0A_list2%20%3D%20%5B2,1,4,6,7%5D%0A%0Alist1%20%3D%20lst2link%28_list1%29%0Alist2%20%3D%20lst2link%28_list2%29%0A%0Av%20%3D%20%5B%5D%0A%0Awhile%20list1%20is%20not%20None%3A%0A%20%20%20%20v.append%28list1.val%29%0A%20%20%20%20list1%20%3D%20list1.next%0A%20%20%20%20%0Awhile%20list2%20is%20not%20None%3A%0A%20%20%20%20v.append%28list2.val%29%0A%20%20%20%20list2%20%3D%20list2.next%0A%0Av%20%3D%20sorted%28v%29%0Am%20%3D%20lst2link%28v%29&cumulative=false&curInstr=191&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false
'''

# CODE ON LEETCODE
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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
        return dummy.next
'''


# CODE TEST
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


_list1 = [1, 2, 3, 4]
_list2 = [2, 1, 4, 6, 7]

list1 = lst2link(_list1)
list2 = lst2link(_list2)

v = []

while list1 is not None:
    v.append(list1.val)
    list1 = list1.next

while list2 is not None:
    v.append(list2.val)
    list2 = list2.next

v = sorted(v)
m = lst2link(v)
