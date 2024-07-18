'''
https://leetcode.com/problems/reorder-list/description/
'''
#%%
from collections import deque
from typing import Optional
from itertools import cycle


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        all_nodes = deque()
        while head:
            all_nodes.append(head)
            head = head.next
        
        head = all_nodes.popleft()
        node = head
        ope = cycle([all_nodes.pop, all_nodes.popleft])
        while all_nodes:
            node.next = next(ope)()
            node = node.next

        node.next = None
        return head

s = Solution()
#%%
l = [1, 2, 3, 4]
#%%
def list_to_link(l):
    head = None
    node = None
    for i in l:
        n = ListNode(i)
        if not node:
            head = n
            node = n
        else:
            node.next = n
            node = n

    return head

head = list_to_link(l)
ans = s.reorderList(head)
# %%
def print_link(ans):
    l = []
    while ans:
        l.append(ans.val)
        ans = ans.next
    return l

print_link(head)
