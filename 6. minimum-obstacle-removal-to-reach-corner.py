'''
https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/
- it is gurnted that --> grid[0][0] == grid[m - 1][n - 1] == 0

'''
#%%
from typing import List
from collections import defaultdict, deque
from functools import lru_cache
from heapq import heappop, heappush


move = (
    (-1, 0),# up
    (+1, 0),# down
    (0, -1),# left
    (0, +1)# right
)
inf = float("inf")
class Solution:
    def valid(self, x, y):
        return self.x>x>=0 and 0<=y<self.y

    def dijkstra(self, x, y):
        pq = []
        heappush(pq, (0, x, y))
        sssp = [[inf]*self.y for _ in range(self.x)]

        visit = set((0, 0))

        while pq:
            dis, x, y = heappop(pq)
            if (x, y) == (self.x-1, self.y-1):
                return dis

            for adx, ady in move:
                cx = x+adx
                cy = y+ady
                if not self.valid(cx, cy): continue
                
                if (cx, cy) in visit: continue
                visit.add((cx, cy))
                
                nd = dis
                if self.grid[cx][cy]:
                    nd+=1

                if nd>sssp[cx][cy]: continue
                sssp[cx][cy] = nd
                heappush(pq, (nd, cx, cy))

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.x = len(grid)# row
        self.y = len(grid[0])# col

        return self.dijkstra(0, 0)

g = Solution()
#%%
g.minimumObstacles(grid = [[0,1,1],[1,1,0],[1,1,0]])
# %%
g.minimumObstacles(grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]])
# %%
