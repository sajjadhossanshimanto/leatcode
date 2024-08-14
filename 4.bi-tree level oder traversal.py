'''
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
'''
#%%
from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        res = [[root.val]]

        stack = deque([root])
        pop_count = 0
        while stack:
            res.append([])
            for _ in range(len(stack)):
                node = stack.popleft()

                if node.left:
                    res[-1].append(node.left.val)
                    stack.append(node.left)
                if node.right:
                    res[-1].append(node.right.val)
                    stack.append(node.right)
        
        if not res[-1]:
            res.pop()

        return res

s = Solution()
# %%
from tree_helper import etu_to_tree, process_tree, draw_graph

t = [3,9,20,None,None,15,7]
t = etu_to_tree(t)

# [[3],[9,20],[15,7]]
s.levelOrder(t)
#%% wa
t = [1,2,3,4,None,None,5]
t = etu_to_tree(t)

# [[1],[2,3],[4,5]]
s.levelOrder(t)
#%%

process_tree(t)
draw_graph(0)
# %%
