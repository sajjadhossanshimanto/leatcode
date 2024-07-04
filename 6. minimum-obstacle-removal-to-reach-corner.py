'''
https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/
- it is gurnted that --> grid[0][0] == grid[m - 1][n - 1] == 0

'''
#%%
from typing import List
from collections import defaultdict


move = (
    (-1, 0),# up
    (+1, 0),# down
    (0, -1),# left
    (0, +1)# right
)
inf = float("inf")
class Solution:
    def valid(self, x, y):
        return self.x<x>=0 and 0<y<self.y

    def dfs(self, x, y, cost):
        if (x, y) == (self.x-1, self.y-1):
            self.min_cost = min(cost, self.min_cost)
            return
        
        self.visit[x][y] = 1
        if self.grid[x][y]:
            cost+= 1

        for adx, ady in move:
            cx = x+adx
            cy = y+ady
            if not self.valid(cx, cy): continue
            if self.visit[cx][cy]: continue

            self.dfs(cx, cy, cost)
        
        # return x, y# TODO: is it guranted x y is valid and not a brick

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.x = len(grid)# row
        self.y = len(grid[0])# col

        self.visit = [[0]*self.y for _ in range(self.x)]
        self.min_cost = inf

        self.dfs(0, 0, 0)
        return self.min_cost

#%%
Solution().minimumObstacles(grid = [[0,1,1],[1,1,0],[1,1,0]])
# %%
