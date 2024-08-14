'''
https://leetcode.com/problems/binary-search-tree-iterator/description/
'''
#%%
from typing import List, Optional
from collections import deque


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inoder = deque()
        
        def dfs(node):
            if node.left: dfs(node.left)
            self.inoder.append(node.val)
            if node.right: dfs(node.right)
        

        dfs(root)

    def next(self) -> int:
        return self.inoder.popleft()

    def hasNext(self) -> bool:
        return bool(self.inoder)

s = BSTIterator()
# %%
from tree_helper import etu_to_tree


t = [7, 3, 15, None, None, 9, 20]
