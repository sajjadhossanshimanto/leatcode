'''
https://leetcode.com/problems/balanced-binary-tree/description/
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        ans = [True]
        def dfs(node):
            l = 0
            if ans[0] and node.left:
                l = dfs(node.left) + 1
            
            r = 0
            if ans[0] and node.right:
                r = dfs(node.right) + 1

            if abs(l-r)>1:
                ans[0]  = False
            
            return max(r, l)
        
        dfs(root)
        return ans[0]

s = Solution()
# %%
from tree_helper import etu_to_tree

t = [3, 9, 20, None, None, 15, 7]
t = etu_to_tree(t)

s.isBalanced(t)
# %%
t = [1,2,2,3,3, None,None,4,4]
t = etu_to_tree(t)

s.isBalanced(t)
# %%
