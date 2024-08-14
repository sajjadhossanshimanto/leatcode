'''
https://leetcode.com/problems/binary-tree-right-side-view/description/
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        ans = []
        level_cache = set()
        def dfs(node, level):
            if not node: return
            if level not in level_cache:
                ans.append(node.val)
                level_cache.add(level)
            
            dfs(node.right, level+1)
            dfs(node.left, level+1)

        dfs(root, 0)
        return ans

s = Solution()
# %%
from tree_helper import etu_to_tree, process_tree, draw_graph

t = [1,2,3,None,5,None,4]
t = etu_to_tree(t)

# [1, 3, 4]
s.rightSideView(t)
# %%
t = [1,None,3]
t = etu_to_tree(t)

[1, 3]
s.rightSideView(t)
# %%
# []
s.rightSideView(None)
# %%
