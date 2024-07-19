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
        
        if len(index)==1:
            return

        if n==1:
            index[-2].next = None
        elif n==len(index):
            head = head.next
        else:
            m = len(index)-n
            index[m-1].next = index[m+1]
        
        return head

s= Solution()
# %%
l = [1, 2, 3, 4, 5]
#%% wa
l = [1]
#%%
from link_helper import list_to_link, print_link


head = list_to_link(l)
ans = s.removeNthFromEnd (head, 1)
print_link(ans)
# %%
