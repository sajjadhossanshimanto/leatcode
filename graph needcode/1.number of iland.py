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

        visit = [[0]*gy for _ in range(gx)]
        def dfs(x, y):
            # print(x, y)
            visit[x][y] = 1

            for adx, ady in move:
                cx, cy = (x+adx, y+ady)
                if not is_valid(cx, cy): continue
                if grid[cx][cy]=="0": continue

                if visit[cx][cy]==0:
                    dfs(cx, cy)
        
        cc=0
        for x in range(gx):
            for y in range(gy):
                if visit[x][y]: continue
                if grid[x][y]=="1":
                    dfs(x, y)
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
