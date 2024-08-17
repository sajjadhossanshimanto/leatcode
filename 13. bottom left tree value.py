'''
https://leetcode.com/problems/find-bottom-left-tree-value/description/
'''
#%%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root) -> int:
        if not root: return 

        max_level = [0]
        ans = [None]
        def dfs(node, lev):
            if lev> max_level[0]:
                ans[0] = node.val
                max_level[0] = lev
            
            if node.left: dfs(node.left, lev+1)
            if node.right: dfs(node.right, lev+1)
        
        dfs(root, 1)
        return ans[0]