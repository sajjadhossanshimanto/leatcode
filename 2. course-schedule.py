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
        
        visit = set()
        def back_edge(node):
            visit.add(node)

            for child in adj[node]:
                if child in visit:
                    # as graph is directed. parent is also a back edge
                    return True

                if back_edge(child):
                    return True                
                adj[node].remove(child)
        
        for i in range(numCourses):
            if not adj[i]: continue

            visit.clear()
            if back_edge(i):
                return False

        return True

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
# %% wa41
# ex = false
# out = true
g.canFinish(20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]])
# proablem is multiple cc
#%% wa37
# ex = true
g.canFinish(3, [[0,1],[0,2],[1,2]])
