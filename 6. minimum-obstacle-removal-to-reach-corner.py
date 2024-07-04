'''
https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/description/
- it is gurnted that --> grid[0][0] == grid[m - 1][n - 1] == 0

'''
#%%
from typing import List
from heapq import heappop, heappush


move = (
    (-1, 0),# up
    (+1, 0),# down
    (0, -1),# left
    (0, +1)# right
)
inf = float("inf")
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        row = len(grid)# row
        col = len(grid[0])# col

        def valid(x, y):
            return row>x>=0 and 0<=y<col
        
        def dijkstra(x, y):
            pq = []
            heappush(pq, (0, x, y))
            sssp = [[inf]*col for _ in range(row)]

            visit = set((0, 0))

            while pq:
                dis, x, y = heappop(pq)
                if (x, y) == (row-1, col-1):
                    return dis

                for adx, ady in move:
                    cx = x+adx
                    cy = y+ady
                    if not valid(cx, cy): continue
                    
                    if (cx, cy) in visit: continue
                    visit.add((cx, cy))
                    
                    nd = dis
                    if grid[cx][cy]:
                        nd+=1

                    if nd>sssp[cx][cy]: continue
                    sssp[cx][cy] = nd
                    heappush(pq, (nd, cx, cy))

        return dijkstra(0, 0)

g = Solution()
#%%
# ans = 2
g.minimumObstacles(grid = [[0,1,1],[1,1,0],[1,1,0]])
# %%
# ans = 0
g.minimumObstacles(grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]])
# %%
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        distance = [[float('inf') for _ in range(n)] for _ in range(m)]
        distance[0][0] = 0
        q = collections.deque([(0, 0, 0)])
        while q:
            d, i, j = q.popleft()
            if i == m - 1 and j == n - 1: return d
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ci, cj = i + di, j + dj
                if 0 <= ci < m and 0 <= cj < n:
                    if d + grid[ci][cj] < distance[ci][cj]:
                        distance[ci][cj] = d + grid[ci][cj]
                        if grid[ci][cj] == 1: q.append((distance[ci][cj], ci, cj))
                        else: q.appendleft((distance[ci][cj], ci, cj))
        return distance[m - 1][n - 1]
        