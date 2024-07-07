'''
https://leetcode.com/problems/course-schedule/
- actually cykcle ditection
'''
#%%
from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        
        intime = [0]*numCourses
        # lowtime = [0]*numCourses
        def dfs(node, parent, time=1):
            intime[node] = time
            # lowtime[node] = time

            for child in adj[node]:
                if intime[child]:# if visited
                    if child!=parent:
                        # an ansistor
                        return False
                    continue

                time+=1
                r = dfs(child, parent, time)
                # lowtime[node] = min()
                if r==False: return r

        r=dfs(0, -1)
        return r==None or r

g = Solution()
#%%
# ans = true
g.canFinish(numCourses = 2, prerequisites = [[1,0]])
# %%
# ans = false
g.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]])
# %% wa
# ans = 1
# out = 0
g.canFinish(numCourses = 2, prerequisites = [[0, 1]])
# %%
