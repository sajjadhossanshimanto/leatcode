'''
https://leetcode.com/problems/max-area-of-island/
'''
#%%
from typing import List
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        gx, gy = len(grid), len(grid[0])

        def bfs(x, y):
            grid[x][y] = 0

            q = deque()
            q.append((x, y, 1))
            ans = 0
            while q:
                x, y, level = q.popleft()
                ans = max(ans, level)

                for cx, cy in (
                    (x+1, y),
                    (x-1, y),
                    (x, y+1),
                    (x, y-1)
                ):
                    if 0<=cx<gx and 0<=cy<gy and grid[cx][cy]:
                        q.append((cx, cy, level+1))
                        grid[cx][cy] = 0

            return ans

        ans = 0
        for x in range(gx):
            for y in range(gy):
                if grid[x][y]:
                    ans = max(bfs(x, y), ans)
                    print(x, y, "-->", ans)
        return ans


g = Solution()
#%%
g.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])
# %%
