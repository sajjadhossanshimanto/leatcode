#%%
from collections import deque
from typing import List


inf = float("inf")
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        gx, gy = len(grid), len(grid[0])

        q=deque()
        q.append((0,0))
        ans = -inf
        visit = set()
        while q:
            x, y = q.popleft()
            ans = max(ans, grid[x][y])

            minv = inf
            for cx, cy in (
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1)
            ):
                if cx<0 or cy<0 or cx==gx or cy==gy or (cx, cy) in visit: continue
                visit.add((cx, cy))

                if (cx, cy) == (gx-1, gy-1):
                    return max(ans, grid[cx][cy])
                
                if grid[cx][cy]<minv:
                    minv = grid[cx][cy]
                    q.appendleft((cx, cy))
                else:
                    q.append((cx, cy))


g=Solution()
#%%
g.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])
# %% wa17
# ans = 14
# out = 15
g.swimInWater([[10,12,4,6],[9,11,3,5],[1,7,13,8],[2,0,15,14]])

# %%
