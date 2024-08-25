'''
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
- min node count 1
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        def dfs(node, path):
            path.append (node.val)
            if node.right==None and node.left==None:
                a = int("".join(map(str, path)))
                ans[0] += a
            else:
                if node.right: 
                    dfs(node.right, path)
                    path.pop()
                if node.left: 
                    dfs(node.left, path)
                    path.pop()
        
        dfs(root, [])
        return ans[0]

s = Solution()
# %%
from tree_helper import list_to_bitree, process_tree, draw_graph

t = [1, 2, 3]
t = list_to_bitree(t)
s.sumNumbers(t)
# %%
process_tree(t)
draw_graph(t)
