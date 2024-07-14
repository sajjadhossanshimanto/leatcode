'''
https://leetcode.com/problems/swim-in-rising-water/description/
'''
#%%deque
from typing import List
from collections import deque
from heapq import heappush, heappop


inf = float("inf")
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        gx, gy = len(grid), len(grid[0])
        visit = [[0]*gy for _ in range(gx)]

        q = []
        heappush(q, (-inf, 0, 0))
        visit[0][0] = 1# cummon midtaked by me. often forgets to add inital node to visit
        while q:
            mx_elevation, x, y = heappop(q)
            if (x, y) == (gx-1, gy-1):# reached end 
                return mx_elevation

            for cx, cy in (
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1)
            ):
                if cx<0 or cy<0 or cx==gx or cy==gy or visit[cx][cy]:
                    continue
                visit[x][y] = 1

                heappush(q, (max(mx_elevation, grid[cx][cy]), cx, cy))

        return -1

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

