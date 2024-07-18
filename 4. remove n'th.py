'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
'''
#%%
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        index = []
        node = head
        while node:
            index.append(node)
            node = node.next
        
        index[len(index)-n-1].next = index[len(index)-n+1]
        return head

s= Solution()
# %%
l = [1, 2, 3, 4, 5]
#%%
l = [1]
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
ans = s.removeNthFromEnd (head, 1)
# %%
def print_link(ans):
    l = []
    while ans:
        l.append(ans.val)
        ans = ans.next
    return l

print_link(head)

# %%
