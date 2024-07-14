'''
https://leetcode.com/problems/swim-in-rising-water/description/
'''
#%%deque
from typing import List
from collections import deque


inf = float("inf")
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        gx, gy = len(grid), len(grid[0])

        visit = [[0]*gy for _ in range(gx)]
        q = deque()
        ans = [inf]
        def dfs(x, y):
            visit[x][y] = 1
            if (cx, cy) == (gx-1, gy-1):# reached end 
                return min(grid[x][y], ans[0])

            min_value = inf
            min_node = None
            for cx, cy in (
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1)
            ):
                if cx<0 or cy<0 or cx==gx or cy==gy or visit[cx][cy]:
                    continue
                
                if grid[cx][cy]<min_value: # whta if equal
                    min_node = (cx, cy)
            
            dfs(*min_node)

        return ans

g=Solution()
#%%

def print_grid(matrix):
    # chould have use pandas dataframe print function
    print(*matrix, sep="\n")
    print()

#%%
l=[[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
g.swimInWater(l)
# print_grid(l)
# %% wa17
# ans = 14
# out = 15
g.swimInWater([[10,12,4,6],[9,11,3,5],[1,7,13,8],[2,0,15,14]])

