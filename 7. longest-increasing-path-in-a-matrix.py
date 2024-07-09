'''
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
'''
#%%
from typing import List
from operator import gt, lt


def print_grid(matrix):
    # chould have use pandas dataframe print function
    print(*matrix, sep="\n")
    print()


move = (
    (0, 1),# right
    (1, 0),# down
    (0, -1),# left
    (-1, 0)# up
)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix)==1 and len(matrix[0])==1:
            return 1

        gx = len(matrix)
        gy = len(matrix[0])
        
        def isvalid(x, y):
            return 0<=x<gx and 0<=y<gy

        visit = [[0]*gy for _ in range(gx)]
        def dfs(x, y):
            visit[x][y]=1
            print(matrix[x][y])
            print_grid(visit)

            ans = 1# this node itself
            for adx, ady in move:
                cx, cy = (x+adx, y+ady)
                if not isvalid(cx, cy): continue
                if visit[cx][cy]: continue
            
                if op(matrix[x][y], matrix[cx][cy]):
                    # child+=1# for this child itself
                    ans=max(dfs(cx, cy)+1, ans)
        
            print(f"{matrix[x][y]} ans->", ans)
            return ans

        op = None
        ans = 0
        for x in range(gx):
            for y in range(gy):
                if visit[x][y]: continue

                for adx, ady in move:
                    cx, cy = (x+adx, y+ady)
                    if not isvalid(cx, cy): continue
                    if visit[cx][cy]: continue
                    if matrix[x][y] == matrix[cx][cy]: continue

                    if matrix[x][y] > matrix[cx][cy]:
                        op = gt
                    elif matrix[x][y] < matrix[cx][cy]:
                        op = lt
                    print(op)
                    r = dfs(x, y)
                    ans = max(ans, r)
        
        return ans

g = Solution()
#%%
# ans = 4
g.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])
#%%
# ans = 4
g.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]])
#%%
# ans = 1
g.longestIncreasingPath([[1]])
#%% wa28
# ans = 3
g.longestIncreasingPath([[1,2],[2,3]])
#%%
g.longestIncreasingPath
g.longestIncreasingPath