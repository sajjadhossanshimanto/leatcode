'''
https://leetcode.com/problems/add-two-numbers/description/
'''
#%%
from typing import Optional
from collections import deque


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = None
        index1 = deque()
        index2 = deque()
        while l1 or l2:
            if l1:
                index1.appendleft(l1.val)
                l1 = l1.next
            if l2:
                index2.appendleft(l2.val)
                l2 = l2.next

        # this step can be improved with one loop
        num1 = int("".join(index1))
        num2 = int("".join(index2))
        ans = str(num1 + num2)
        
        head = node = None
        for i in range(ans):
            if not head:
                node = head = ListNode(int(i))
            else:
                node.next = ListNode(int(i))
                node = node.next

s = Solution()
# %%
