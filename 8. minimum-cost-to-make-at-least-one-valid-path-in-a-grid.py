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
                if (adx, ady)!=move_map[grid[cx][cy]-1]:
                    nd+=1

                if nd>=distance[cx][cy]: continue

                if dis==nd:# same check
                    q.appendleft((dis, cx, cy))
                else:
                    q.append((dis+1, cx, cy))

        return 0

g = Solution()
# %%
# ans = 3
g.minCost(grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]])
# %%
# ex = 0
# out = 2
g.minCost(grid = [[1,1,3],[3,2,2],[1,1,4]])
# %%
