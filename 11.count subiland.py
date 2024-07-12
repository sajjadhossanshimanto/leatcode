'''
https://leetcode.com/problems/count-sub-islands/description/
'''
#%%
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        gx, gy = len(grid1), len(grid1[0])

        visit = [[0]*gy for _ in range(gx)]
        def dfs(x, y, plus):
            visit[x][y] = 1

            for cx, cy in (
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1)
            ):
                if cx<0 or cy<0 or cx==gx or cy==gy or visit[cx][cy] or grid2[cx][cy]==0:
                    continue
                
                if grid1[cx][cy]==0:
                    plus = 0
                
                plus = dfs(cx, cy, plus)# once plus is set to zero thers no way to become 1 again
            
            return plus

        cc=0
        for x in range(gx):
            for y in range(gy):
                if grid1[x][y] and grid2[x][y] and visit[x][y]==0:
                    cc+=dfs(x, y, 1)
                    # print(x, y, "-->", cc)
                    
        return cc

g= Solution()
#%%
# ans = 3
g.countSubIslands(grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]])
 # %% wa17
# ex = 6
# out = 7
g.countSubIslands(
    grid1=[[1,0,1,0,1,1,1,0,1,1,0,1,1,1,1],[1,1,1,1,1,0,1,1,1,1,0,0,0,1,1],[1,1,1,1,1,0,1,1,1,1,1,1,1,1,0],[1,1,1,1,0,1,0,0,1,1,1,1,0,0,1],[0,0,1,1,1,1,1,0,1,0,1,1,1,0,0],[0,1,1,1,1,1,1,1,1,0,1,1,1,1,1],[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,0,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,0,1,0,0,1,1,1,0,0,1,1],[1,0,1,1,1,1,1,0,0,1,1,1,1,0,1],[0,1,0,0,0,1,1,1,1,1,1,1,0,0,1]],
    grid2=[[1,0,1,0,0,0,1,0,0,0,0,0,1,0,1],[1,1,0,1,0,1,1,1,1,1,0,1,0,1,1],[1,1,1,0,1,1,1,1,1,1,0,1,0,1,1],[1,0,0,1,0,1,1,1,0,0,1,0,1,0,1],[0,1,1,1,1,1,1,0,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,1,1,1,0,1,1,1,0],[1,1,1,1,1,1,1,1,1,0,0,1,0,1,1],[1,0,1,0,0,1,1,1,0,1,0,1,1,1,1],[0,1,0,1,1,1,0,1,1,1,1,0,0,0,1],[1,1,1,0,1,0,0,0,1,1,0,0,1,1,1],[1,0,0,1,1,1,0,0,0,0,1,0,1,0,0],[0,0,1,1,1,1,1,0,1,0,1,1,1,0,0]]
)

# %%