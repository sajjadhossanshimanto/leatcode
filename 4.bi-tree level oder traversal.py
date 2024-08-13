'''
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
'''
#%%
from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        res = [[root.val]]

        stack = deque([root])
        pop_count = 0
        while stack:
            node = stack.popleft()
            pop_count += 1
            if pop_count==2:
                res.append([])
                pop_count = 0

            if node.left:
                res[-1].append(node.left.val)
                stack.append(node.left)
            if node.right:
                res[-1].append(node.right.val)
                stack.append(node.right)

        while not res[-1]:
            res.pop()

        return res

s = Solution()
# %%
from tree_helper import etu_to_tree, process_tree, draw_graph

t = [3,9,20,None,None,15,7]
t = []
t = [1,2,3,4,None,None,5]
t = etu_to_tree(t)

s.levelOrder(t)
# %%
process_tree(t)
draw_graph(0)
# %%
