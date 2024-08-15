'''
https://leetcode.com/problems/convert-bst-to-greater-tree/
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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return 

        def dfs(node, pre):
            r = pre
            if node.right:
                r = dfs(node.right, pre)
            node.val+=r

            if node.left:
                return  dfs(node.left, node.val)            
            return node.val

        dfs(root, 0)
        
        return root

s = Solution()
#%%
from tree_helper import etu_to_tree, process_tree, draw_graph

t = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
t = etu_to_tree(t)

# [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
t = s.convertBST(t)
process_tree(t)
# %%
t = [0, None, 1]