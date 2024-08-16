'''
https://leetcode.com/problems/flip-equivalent-binary-trees/

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
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1==None and root2==None:
            return True
        if not (root1 and root2):
            return False

        if root1.val != root2.val:
            return False

        if not self.flipEquiv(root1.left, root2.right):
            return False
        if not self.flipEquiv(root1.right, root2.left):
            return False

        return True

s = Solution()
#%%
from tree_helper import etu_to_tree, process_tree, draw_graph

t1 = [1,2,3,4,5,6,None,None,None,7,8]
t2 = [1,3,2,None,6,4,5,None,None,None,None,8,7]
# %%
t1 = etu_to_tree(t1)
t2 = etu_to_tree(t2)
s.flipEquiv(t1, t2)
#%%
process_tree(t)
draw_graph()
# %%
