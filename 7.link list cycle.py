'''
https://leetcode.com/problems/linked-list-cycle/description/
'''
#%%
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
            if node.val in visit:
                return True

            visit.add(node.val)
            node = node.next
        
        return False

# %%
