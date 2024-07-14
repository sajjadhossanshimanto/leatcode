'''
https://leetcode.com/problems/rotting-oranges/description/
'''
#%%
from typing import List
from collections import deque


def print_grid(l):
    print(*l, sep = '\n')
    print()

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        gx, gy = len(grid), len(grid[0])
        q = deque()

        fresh = 0
        for x in range(gx):
            for y in range(gy):
                if grid[x][y]==2:
                    q.append((x, y))
                if grid[x][y]==1:
                    fresh+=1

        time = 0
        # it is actually guranted that their wouls be no more rotten orange
        while q:
            for _ in range(len(q)):# in for loop range( ) actually takes the snaps of len(q). it is not changed accordingly
                x, y = q.popleft()

                for cx, cy in (
                    (x+1, y),
                    (x-1, y),
                    (x, y+1),
                    (x, y-1)
                ):
                    if cx<0 or cy<0 or cx==gx or cy==gy or grid[cx][cy]!=1:
                        continue
                    grid[cx][cy] = 0# trick visit list

                    q.append((cx, cy))
                    fresh -= 1
            time+=1


        return -1 if fresh else time


g = Solution()
#%%
# ans = 4
g.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
#%%
# ans = -1
g.orangesRotting([[2,1,1],[0,1,1],[1,0,1]])
#%%
# ans = 0
g.orangesRotting([[0,2]])
# %% wa146
# ans = 4
# out = 3
g.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
# %% wa169
# ans = 2
# out = 3
g.orangesRotting([[2,1,1],[1,1,1],[0,1,2]])
# %%