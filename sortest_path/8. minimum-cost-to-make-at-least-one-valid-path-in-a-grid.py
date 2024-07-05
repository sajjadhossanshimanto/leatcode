'''
https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/
- zero indexed
'''
#%%
from typing import List
from collections import deque


move_map = (
    (0, +1),
    (0, -1),
    (+1, 0),
    (-1, 0)
)
inf = float('inf')
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        gx = len(grid)
        gy = len(grid[0])
        def valid_path(x, y):
            return 0<=x<gx and 0<=y<gy
        
        distance = [[inf]*gy for _ in range(gx)]
        distance[0][0] = 0
        q = deque()
        q.append((0, 0, 0))
        #         dis, (pos)
        while q:
            dis, x, y = q.popleft()
            if (x, y)==(gx-1, gy-1):
                return dis

            for adx, ady in move_map:
                cx, cy = (x+adx, y+ady)
                if not valid_path(cx, cy): continue

                nd = dis
                if (adx, ady)!=move_map[grid[x][y]-1]:
                    nd+=1

                if nd<distance[cx][cy]:
                    distance[cx][cy]=nd

                    if dis==nd:# same check
                        q.appendleft((nd, cx, cy))
                    else:
                        q.append((nd, cx, cy))

        return distance[gx-1][gy-1]

g = Solution()
# %%
# ans = 3
g.minCost(grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]])
# %%
# ex = 0
# out = 2 ----fixed
g.minCost(grid = [[1,1,3],[3,2,2],[1,1,4]])
# %%
# ans = 1
g.minCost([[1,2],[4,3]])
# %%
# approach --> manual deque with 2 list

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = [(m-1,n-1)]
        potential = []
        cost = 0
        while True:
            for x,y in queue:
                if x == 0 and y == 0:
                    return cost
                if grid[x][y] > 0:
                    grid[x][y] = 0
                    if x > 0:
                        if grid[x-1][y] == 3:
                            queue.append((x-1,y))
                        elif grid[x-1][y] > 0:
                            potential.append((x-1,y))
                    if x < m-1:
                        if grid[x+1][y] == 4:
                            queue.append((x+1,y))
                        elif grid[x+1][y] > 0:
                            potential.append((x+1,y))
                    if y > 0:
                        if grid[x][y-1] == 1:
                            queue.append((x,y-1))
                        elif grid[x][y-1] > 0:
                            potential.append((x,y-1))
                    if y < n-1:
                        if grid[x][y+1] == 2:
                            queue.append((x,y+1))
                        elif grid[x][y+1] > 0:
                            potential.append((x,y+1))
            cost += 1
            queue = potential
            potential = []