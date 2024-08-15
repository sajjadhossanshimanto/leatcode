'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
'''
#%%
from typing import List, Optional


inf = float('inf')
class Solution:
    def maxPathSum(self, root) -> int:
        ans = [-inf]
        def dfs(node):
            if not node: return 0

            l = dfs(node.left)
            r = dfs(node.right)

            # with attached
            ans[0] = max(ans[0], node.val+r+l)
            # without attached
            ans[0] = max(ans[0], node.val)

            # among all return the max possible
            return max(node.val+max(l,r), node.val)
        
        ans[0] = max(dfs(root), ans[0])
        return ans[0]

s = Solution()
# %%
from tree_helper import etu_to_tree, process_tree, draw_graph

t = [1, 2, 3]
t = etu_to_tree(t)

# 6
s.maxPathSum(t)
# %%
t = [-10,9,20,None,None,15,7]
t = etu_to_tree(t)

# 42
s.maxPathSum(t)
# %% wa65
t = [-3]
# ans = -3
# out = 0
# %% wa69
t = [2, -1]
t = etu_to_tree(t)

# 2
s.maxPathSum(t)
#%%%
t = [1, -2, 3]
t = etu_to_tree(t)

# 4
s.maxPathSum(t)
# %% wa 
t = [-1,-2,10,-6,None,-3,-6]
t = etu_to_tree(t)

# 10
s.maxPathSum(t)
# %%
draw_graph()
# %%
