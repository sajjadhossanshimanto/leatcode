'''
https://leetcode.com/problems/construct-string-from-binary-tree/
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if node.val==None: return ""
            
            l = [str(node.val)]
            if node.left:
                r = dfs(node.left)
                l.append(f"({r})")
            
            if  node.right:
                if not node.left:
                    l.append("()")
                
                r = dfs(node.right)
                l.append(f"({r})")

            # while
            return "".join(l)
        
        return dfs(root)

s = Solution()
# %%
from tree_helper import etu_to_tree, draw_graph, process_tree

t = [1, 2, 3, 4]
t = etu_to_tree(t)

"1(2(4))(3)"
s.tree2str(t)
#%% wa36
t = [1,2,3,None,4]
t = etu_to_tree(t)

"1(2()(4))(3)"
s.tree2str(t)
#%%
process_tree(t)
draw_graph()
# %%
