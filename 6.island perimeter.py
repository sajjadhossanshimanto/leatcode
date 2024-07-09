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

        def is_valid(x, y):
            return 0<=x<gx and 0<=y<gy and grid[x][y]
        
        visit = set()
        def dfs(x, y):
            visit.add((x, y))
            # print(x, y)

            edge = 4
            for cx, cy in move:
                cx+=x
                cy+=y
                if is_valid(cx, cy):
                    if (cx, cy) not in visit:
                        edge = edge-1+dfs(cx, cy)
            
            # print((x, y), "edge ->", edge)
            return edge


        for x in range(gx):
            for y in range(gy):
                # if (x, y) not in visit:
                return dfs(x, y)

g = Solution()
#%%
g.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
# %%
