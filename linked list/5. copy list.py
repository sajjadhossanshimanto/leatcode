'''
https://leetcode.com/problems/copy-list-with-random-pointer/description/
'''
#%%
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from copy import deepcopy


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return deepcopy(head)