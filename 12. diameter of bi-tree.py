'''
https://leetcode.com/problems/diameter-of-binary-tree/description/
- it may or nay not involve root
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

        ans = [0]
        def dfs(node):
            l, r = 0, 0
            if node.left: l = dfs(node.left) + 1
            if node.right: r = dfs(node.right) + 1

            ans[0] = max(ans[0], l+r)
            return max(l, r)

        dfs(root)
        return ans[0]

s = Solution()
# %%
from tree_helper import etu_to_tree, process_tree,draw_graph

# # 3
t= [1,2,3,4,5]
t = etu_to_tree(t)
s.diameterOfBinaryTree(t)

#%%
# # 1
t = [1, 2]
t = etu_to_tree(t)
s.diameterOfBinaryTree(t)

#%%
# 8
t = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
t = etu_to_tree(t)
# s.diameterOfBinaryTree(t)

process_tree(t)
# %%
draw_graph()
# %%
