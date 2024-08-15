'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
'''
#%%
from typing import List, Optional


inf = float('inf')
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [-inf]
        def dfs(node):
            if not node: return 0

            l = dfs(node.left)
            r = dfs(node.right)

            ans[0] = max(ans[0], node.val+r+l)

            return node.val+max(l,r)
        
        dfs(root)
        return ans[0]

s = Solution()
# %%
from tree_helper import etu_to_tree

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
