'''
https://leetcode.com/problems/triangle/description/
'''
#%%
from typing import List, Optional

inf = float("inf")
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        gx, gy = len(triangle)-1, len(triangle[-1])-1

        ans = [inf]
        def dfs(x, y, pre_sum):
            pre_sum+=triangle[x][y]

            if x==gx:
                # leaf node. no left & right
                ans[0] = min(ans[0], pre_sum)
            else:
                # chek if left & if right
                dfs(x+1, y, pre_sum)
                if y<gy:
                    # there exist left
                    dfs(x+1, y+1, pre_sum)
                # if y=0:

        dfs(0, 0, 0)
        return ans[0]

s = Solution()
# %%
from tree_helper import list_to_bitree, process_tree, draw_graph

t = [[2],[3,4],[6,5,7],[4,1,8,3]]
s.minimumTotal(t)
# %%
t = [[-10]]
s.minimumTotal(t)
# %%
