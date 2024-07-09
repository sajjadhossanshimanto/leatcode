'''
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
sol -> https://www.youtube.com/watch?v=wCc_nd-GiEc
'''
#%%
from typing import List


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

        dp = {}# he don't uses such double defaultdict
        def dfs(x, y):
            if (x, y) in dp:
                return dp[(x, y)]

            ans = 1
            for adx, ady in move:
                cx, cy = (x+adx, y+ady)
                if not isvalid(cx, cy): continue
                
                if matrix[cx][cy]>matrix[x][y]:
                    ans = max(ans, dfs(cx, cy)+1)
            
            dp[(x, y)] = ans
            return ans
        
        for x in range(gx):
            for y in range(gy):
                if dp.get((x, y)): continue

                dfs(x, y)
        
        return max(dp.values())# he sas its the same as tracking max with avariable



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
#%% wa35
# ans = 6
# out = 4
g.longestIncreasingPath([[7,8,9],[9,7,6],[7,2,3]])
#%% wa128
# ans = 8
# out = 7
g.longestIncreasingPath([[19,2,8,6,4,14,1,0,17],[0,1,9,10,11,4,12,14,5],[14,12,16,0,15,8,5,2,8],[5,4,1,17,9,18,8,5,2],[9,5,4,8,16,7,11,5,0],[5,7,14,18,10,0,14,14,0],[9,14,4,13,18,16,9,12,10],[18,13,9,18,11,4,12,10,10],[7,14,16,19,10,19,11,6,4],[16,2,3,7,15,9,7,1,1],[1,6,16,15,18,6,6,1,14],[9,5,2,9,8,3,2,3,10],[2,3,16,8,7,7,0,18,16],[11,0,16,8,13,13,11,3,8],[17,11,0,12,11,15,12,17,0]])
#%%
g.longestIncreasingPath
g.longestIncreasingPath