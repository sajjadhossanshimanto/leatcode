'''
https://leetcode.com/problems/island-perimeter/
'''
#%%
from typing import List


move = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
)
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        gx, gy = len(grid), len(grid[0])
        
        visit = set()
        def dfs(x, y):
            visit.add((x, y))
            # print(x, y)

            edge = 4
            for cx, cy in move:
                cx+=x
                cy+=y
                if 0<=cx<gx and 0<=cy<gy and grid[cx][cy]:
                    if (cx, cy) in visit:
                        edge-=1
                    else:
                        edge = edge-1+dfs(cx, cy)
            
            # print((x, y), "edge ->", edge)
            return edge


        for x in range(gx):
            for y in range(gy):
                # if (x, y) not in visit:
                if grid[x][y]:
                    return dfs(x, y)

g = Solution()
#%%
g.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
# %%
