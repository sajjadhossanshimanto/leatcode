'''
https://leetcode.com/problems/maximum-depth-of-binary-tree
'''
#%%
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        stack = deque()
        stack.append(root)
        level = 0
        while stack:
            level+=1
            for _ in range(len(stack)):
                node = stack.popleft()
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
        
        return level