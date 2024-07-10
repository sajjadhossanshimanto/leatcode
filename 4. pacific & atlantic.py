'''
https://leetcode.com/problems/pacific-atlantic-water-flow/description/
'''
#%%
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p = set()
        a = set()

        gx, gy = len(heights), len(heights[0])

        def dfs(x, y, visit):
            visit.add((x, y))

            for cx, cy in (
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1),
            ):
                if 0<=cx<gx and 0<=cy<gy and (cx, cy) not in visit:
                    if heights[cx][cy]>=heights[x][y]:
                        dfs(cx, cy, visit)

        x = 0
        for y in range(gy):
            dfs(x, y, p)
        y = 0
        for x in range(gx):
            dfs(x, y, p)
        
        x = gx-1
        for y in range(gy):
            dfs(x, y, a)
        y = gy-1
        for x in range(gx):
            dfs(x, y, a)
        
        return sorted(list(a&p))

g=Solution()
#%%
g.pacificAtlantic( [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
# %%
