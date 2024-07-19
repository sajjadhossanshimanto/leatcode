'''
https://leetcode.com/problems/merge-two-sorted-lists/description/
'''
#%%
from typing import Optional
from heapq import heappush, heappop


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        index = []
        while list1 or list2:
            if list1:
                heappush(index, list1.val)
                list1 = list1.next
            if list2:
                heappush(index, list2.val)
                list2 = list2.next
        
        head = ListNode(heappop(index))
        node = head
        while index:
            node.next = ListNode(heappop(index))
            node = node.next

        return head

s = Solution()
# %%
from link_helper import list_to_link, print_link

l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
ans = s.mergeTwoLists(list_to_link(l1), list_to_link(l2))
print_link(ans)
# %%
