#%%
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        gx, gy = len(grid1), len(grid1[0])

        visit = set()
        def dfs(x, y):
            if x<0 or y<0 or x==gx or y==gy or (x, y) in visit or grid1[x][y]==0 or grid2[x][y]==0:
                return
            visit.add((x, y))

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)
        
        cc=0
        for x in range(gx):
            for y in range(gy):
                if grid1[x][y] and grid2[x][y] and (x, y) not in visit:
                    dfs(x, y)
                    print(x, y)
                    cc+=1
        return cc

g= Solution()
#%%
g.countSubIslands(grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]])
# %%
