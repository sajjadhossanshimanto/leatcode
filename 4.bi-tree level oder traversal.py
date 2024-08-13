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
        while stack:
            node = stack.popleft()
            l = []
            if node.left:
                l.append(node.left.val)
                stack.append(node.left)
            if node.right:
                l.append(node.right.val)
                stack.append(node.right)
            
            if l: res.append(l)

        return res

s = Solution()
# %%
from tree_helper import etu_to_tree

t = [3,9,20,None,None,15,7]
t = []
t = etu_to_tree(TreeNode(None))

s.levelOrder(t)
# %%
