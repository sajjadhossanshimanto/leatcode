'''
https://leetcode.com/problems/reverse-linked-list/
'''
#%%
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        index = []
        while head:
            index.append(head.val)
            head = head.next
        
        head = None
        node = head
        while index:
            n = ListNode(index.pop())
            if not head:
                head = n
                node = n
            else:
                node.next = n

        return head

s = Solution()
# %%
from link_helper import list_to_link, print_link

l=[1, 2, 3, 4, 5]
head = list_to_link(l)
print_link(head)
ans = s.reverseList(head)
print_link(ans)
# %%
