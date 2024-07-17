'''
https://leetcode.com/problems/clone-graph/description/
'''
#%%

from typing import Optional
from copy import deepcopy


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return deepcopy(node)