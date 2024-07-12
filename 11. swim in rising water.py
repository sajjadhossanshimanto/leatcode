#%%
from collections import deque
from typing import List
from heapq import heappop, heappush


inf = float("inf")
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        gx, gy = len(grid), len(grid[0])

        q=[]
        q.append((grid[0][0], 0, 0, -inf))

        visit = set()
        sssp = {}
        ans = inf
        while q:
            dis, x, y, max_ = heappop(q)
            # print(grid[x][y], "-->", dis)

            for cx, cy in (
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1)
            ):
                if (cx, cy) == (gx-1, gy-1):# reached end 
                    ans = min(max_, grid[cx][cy], ans)
                    continue

                if cx<0 or cy<0 or cx==gx or cy==gy or (cx, cy) in visit:
                    continue
                visit.add((cx, cy))

                nd = dis+grid[cx][cy]
                if nd<=sssp.get((cx, cy), inf):
                    sssp[(cx, cy)] = nd
                    heappush(q, (nd, cx, cy, max(max_, grid[cx][cy])))

        return ans

g=Solution()
#%%

def print_grid(matrix):
    # chould have use pandas dataframe print function
    print(*matrix, sep="\n")
    print()

#%%
l=[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
g.swimInWater(l)
# print_grid(l)
# %% wa17
# ans = 14
# out = 15
g.swimInWater([[10,12,4,6],[9,11,3,5],[1,7,13,8],[2,0,15,14]])

# %%
