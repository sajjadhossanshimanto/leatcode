'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
- k is guranted tobe less or equal to n
- k -> 1 indexed
'''
#%%
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        if not root: return 

        ans = []
        def dfs(node):
            if node.left: dfs(node.left)

            ans.append(node.val)
            if len(ans)==k:
                return
            if node.right: dfs(node.right)

        dfs(root)
        return ans[k-1]

s = Solution()
# %%
from tree_helper import etu_to_tree, process_tree, draw_graph

t = [3,1,4,None,2]
t = etu_to_tree(t)
s.kthSmallest(t, 4)
# %%
