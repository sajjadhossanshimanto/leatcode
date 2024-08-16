'''
https://leetcode.com/problems/binary-tree-inorder-traversal/description/
'''
#%%
class Solution:
    def inorderTraversal(self, root):
        if not root: return []

        ans = []
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            ans.append(node.val)
            dfs(node.right)

        dfs(root)
        return ans