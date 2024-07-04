'''
https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/
- it is gurnted that --> grid[0][0] == grid[m - 1][n - 1] == 0

'''
#%%
from typing import List
from collections import defaultdict, deque
from functools import lru_cache


move = (
    (-1, 0),# up
    (+1, 0),# down
    (0, -1),# left
    (0, +1)# right
)
inf = float("inf")
class Solution:
    def valid(self, x, y):
        return self.x>x>=0 and 0<y<self.y

    # @lru_cache
    def dfs(self, x, y):# use dfs to update bfs  value

        # if (x, y) == (self.x-1, self.y-1):
        #     self.min_cost = min(cost, self.min_cost)
        #     return True

        # if self.grid[x][y]:
        #     cost+= 1
        # else:
        self.visit[x][y] = 1

        for adx, ady in move:
            cx = x+adx
            cy = y+ady
            if not self.valid(cx, cy): continue
            if self.visit[cx][cy] or self.grid[cx][cy]: continue

            self.dfs(cx, cy)

        return x, y# TODO: is it guranted x y is valid and not a brick

    def bfs(x, y):
        q = deque()
        q.append((x, y, cost))
        self.level[x][y] = 0

        while q:
            x, y, cost = q.popleft()

            for adx, ady in move:
                cx = x+adx
                cy = y+ady
                # in bfs thers no way going backword
                # so no need of visit
                if not self.valid(cx, cy): continue
                
                child_cost = cost
                if self.grid[cx]c[y]:
                    child_cost+=1

                # if self.level[x][y] == -1:
                self.level[cx][cy] = child_cost
                q.append((cx, cy, child_cost))
                # else:# not going to happen
                #     child_cost<

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.x = len(grid)# row
        self.y = len(grid[0])# col

        # self.debug=[]
        # self.debug.append((cx, cy))
        # self.debug.pop()
        # self.visit = [[0]*self.y for _ in range(self.x)]
        self.min_cost = inf
        self.level = [[-1]*self.y for _ in range(self.x)]

        self.dfs(0, 0, 0)
        return self.min_cost

g = Solution()
#%%
g.minimumObstacles(grid = [[0,1,1],[1,1,0],[1,1,0]])
# %%
g.minimumObstacles(grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]])
# %%
