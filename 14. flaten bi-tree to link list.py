'''
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
'''
#%%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return 

        def dfs(node):
            if not (node.left and node.right):
                return node
            
            if node.left:
                l = dfs(node.left)
                l.right = node.right
                node.right = node.left
                node.left = None# del operation

                if node.right: return dfs(l.right)# avtullay the node.right
                return l
            
            else:
                if node.right: return dfs(node.right)

        dfs(root)
        return root

s = Solution()
# %%
from tree_helper import etu_to_tree, process_tree, draw_graph

t = [1, 2, 5, 3, 4, None, 6]
t = etu_to_tree(t)
t = s.flatten(t)
# %%
process_tree(t)
# %%
draw_graph(t)
# %%
