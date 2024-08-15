'''
https://leetcode.com/problems/diameter-of-binary-tree/description/
'''
#%%
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        def dfs(node):
            if not node: return 0

            return max(dfs(node.left) + 1, dfs(node.right) + 1)

        return dfs(root.left) + dfs(root.right)

s = Solution()
# %%
from tree_helper import etu_to_tree

# # 3
# t= [1,2,3,4,5]

# # 1
# t = [1, 2]

t = etu_to_tree(t)
s.diameterOfBinaryTree(t)
# %%
