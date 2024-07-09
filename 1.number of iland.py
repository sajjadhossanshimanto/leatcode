'''
https://leetcode.com/problems/number-of-islands/
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
    def numIslands(self, grid: List[List[str]]) -> int:
        gx, gy = len(grid), len(grid[0])
        def is_valid(x, y):
            return 0<=x<gx and 0<=y<gy

        visit = set()
        def dfs(x, y):
            visit.add((x, y))

            for adx, ady in move:
                cx, cy = (x+adx, y+ady)
                if not is_valid(cx, cy): continue
                if (cx, cy) in visit: continue

                if grid[cx][cy]:
                    dfs(cx, cy)
        
        cc=0
        for x in range(gx):
            for y in range(gy):
                if (x, y) in visit: continue
                if grid[x][y]:
                    dfs(x, y)
                    print(x, y)
                    cc+=1
        
        return cc

g = Solution()
#%%
# ans = 1
g.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])

# %%
# ans = 3
g.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
# %%
