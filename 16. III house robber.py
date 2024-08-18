'''
https://leetcode.com/problems/house-robber-iii/
'''
#%%
from itertools import cycle
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root) -> int:
        if not root: return 

        stack = deque()
        stack.append(root)
        ans = cycle([[0], [0]])
        while stack:
            total = next(ans)
            for _ in range(len(stack)):
                node = stack.popleft()
                total[0] += node.val
                if node.left: stack.append(node.left)
                if node.right: stack.append(node.right)
        
        return max(next(ans)[0], next(ans)[0])

s = Solution()
# %%
from tree_helper import etu_to_tree, process_tree, draw_graph

# 7
t = [3,2,3,None,3,None,1]

# 9
t = [3,4,5,1,3,None,1]

t = etu_to_tree(t)
s.rob(t)
# %%
