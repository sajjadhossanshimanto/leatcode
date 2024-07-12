'''
https://leetcode.com/problems/rotting-oranges/description/
'''
#%%
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        gx, gy = len(grid), len(grid[0])

        def bfs(x, y):
            q = deque()
            q.append((x, y, 0))
            # level = 0
            ans = 0
            while q:
                x, y, level = q.popleft()
                grid[x][y] = 0
                ans = max(ans, level)
                # print(x, y)

                for cx, cy in (
                    (x+1, y),
                    (x-1, y),
                    (x, y+1),
                    (x, y-1)
                ):
                    if cx<0 or cy<0 or cx==gx or cy==gy:
                        continue

                    if grid[cx][cy]==2:
                    # what if thers 2 rotten in same active 
                        level = 0
                        ans = ans//2
                    if grid[cx][cy]==1:
                        q.append((cx, cy, level+1))
                    
                    grid[cx][cy] = 0
                # print_grid(grid)
            
            return ans

        ans = 0
        for x in range(gx):
            for y in range(gy):
                if grid[x][y]==2:
                    ans = max(bfs(x, y), ans)

        for x in range(gx):
            if 1 in grid[x]: return -1
        
        return ans


g = Solution()
#%%
g.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
# %%
