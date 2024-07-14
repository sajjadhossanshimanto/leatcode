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
# %%
# optimazation
# they avoids visit to get optizised
# here setting grid2 = 0 getd this cell to avoid by grid2==1
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        R, C = len(grid1), len(grid1[0])
        
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid2[r][c] == 0:
                return True
            if grid2[r][c] == 1 and grid1[r][c] == 0:
                return False

            grid2[r][c] = 0
            result = True
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                result = dfs(r + dr, c + dc) and result
            return result

        count = 0
        for i in range(R):
            for j in range(C):
                if grid2[i][j] == 1 and dfs(i, j):
                    count += 1

        return count
