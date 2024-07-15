'''
https://leetcode.com/problems/shortest-bridge/description/
'''
#%%
from typing import List
from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        gx, gy = len(grid), len(grid[0])
        def isValid(x, y):
            return 0<=x<gx and 0<=y<gy

        visit = [[0]*gy for _ in range(gx)]
        source = set()
        def dfs(x, y):
            visit[x][y] = 1

            for cx, cy in (
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1)
            ):
                if isValid(cx, cy):
                    if grid[cx][cy]==0:
                        source.add((x, y))
                    elif not visit[cx][cy]:
                        dfs(cx, cy)

        def bfs():
            q = deque(source)
            res = 0
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    for cx, cy in (
                        (x+1, y),
                        (x-1, y),
                        (x, y+1),
                        (x, y-1)
                    ):
                        if isValid(cx, cy) and visit[cx][cy]==0:
                            if grid[cx][cy]:
                                return res
                            
                            visit[cx][cy] = 1
                            q.append((cx, cy))
                res+=1

        for x in range(gx):
            for y in range(gy):
                if grid[x][y]:
                    dfs(x, y)
                    # return source
                    return bfs()


g = Solution()
# %%
# ans = 1
g.shortestBridge([[0,1],[1,0]])
# %%
ans = 2
g.shortestBridge([[0,1,0],[0,0,0],[0,0,1]])
#%%
ans = 1
g.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])
# %%
