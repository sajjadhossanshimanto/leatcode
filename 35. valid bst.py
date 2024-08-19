'''
https://leetcode.com/problems/validate-binary-search-tree/
'''
#%%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        # if not root: return # node count [1,...]
        if root.left:
            if root.left.val >= root.val: 
                return False
            if not self.isValidBST(root.left): return False
        
        if root.right:
            if root.right.val <= root.val: 
                return False
            if not self.isValidBST(root.right): return False

        return True

s = Solution()
# %%
from tree_helper import list_to_bitree, process_tree, draw_graph

# 1
t = [2, 2, 2]
t = list_to_bitree(t)
s.isValidBST(t)
