'''
https://leetcode.com/problems/max-area-of-island/
'''
#%%
from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        gx, gy = len(grid), len(grid[0])

        def dfs(x, y):
            grid[x][y] = 0

            child_count = 0
            for cx, cy in (
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1)
            ):
                if 0<=cx<gx and 0<=cy<gy and grid[cx][cy]:
                    # grid[cx][cy] = 0
                    child_count += 1
                    child_count += dfs(cx, cy)

            return child_count

        # return dfs(3, 8)
        ans = 0
        for x in range(gx):
            for y in range(gy):
                if grid[x][y]:
                    ans = max(dfs(x, y)+1, ans)
                    # print(x, y, "-->", ans)
        return ans


g = Solution()
#%%
ans = 6
g.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
# %% wa538
# ans = 4
g.maxAreaOfIsland([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]])

# %%
