'''
https://leetcode.com/problems/invert-binary-tree/description/
'''
#%%
class Solution:
    def invertTree(self, root):
        if not root: return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

s = Solution()
# %%
from tree_helper import etu_to_tree, process_tree

t = [4,2,7,1,3,6,9]
t = etu_to_tree(t)
t = s.invertTree(t)
# %%
process_tree(t)

# %%
