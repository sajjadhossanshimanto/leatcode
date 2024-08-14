'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
- poin is it is binary tree
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def dfs(i):
            # 1 indexed
            if not 0<i<=len(preorder):
                return 

            node = TreeNode(preorder[i-1])
            node.left = dfs(2*i)
            node.right = dfs(2*i+1)

            return node

        # 1 indexed
        return dfs(1)
    
s = Solution()
# %%
t = s.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7])
# %%
from tree_helper import process_tree, draw_graph


process_tree(t)
# %%
draw_graph(0)
# %%
