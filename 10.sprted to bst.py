'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(l, r):
            if l>r:
                return None
            
            root = (r+l)//2
            node = TreeNode(nums[root])

            node.left = dfs(l, root-1)
            node.right = dfs(root+1, r)
                
            return node
        
        head = dfs(0, len(nums)-1)
        return head

s = Solution()
# %%
t = s.sortedArrayToBST(nums = [-10,-3,0,5,9])
# %%
from tree_helper import process_tree, draw_graph, G

process_tree(t)
draw_graph()
# %%
