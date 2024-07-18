'''
https://leetcode.com/problems/linked-list-cycle/description/
'''
#%%
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit = set()
        node = head
        while node:
            val = id(node)
            if val in visit:
                return True

            visit.add(val)
            node = node.next
        
        return False

s = Solution()
# %%
l = [1, 2]
#%% wa24
# value may recome repeated
# need to check objects
l = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
#%%
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

# node.next.next = node
# %%
s.hasCycle(head)
# %%
# two pointer approach
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        while(fast and fast.next):
            head = head.next
            fast = fast.next.next
            if head == fast:
                return True          
        return False