'''
https://leetcode.com/problems/course-schedule-ii/description/
- top sort
'''
#%%
from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
        
        visit = set()
        done = set()
        oder = []
        def back_edge(node):
            visit.add(node)

            for child in adj[node]:
                if child in visit:
                    # as graph is directed. parent is also a back edge
                    return True
                if child in done: continue
                
                if back_edge(child):
                    return True
                visit.remove(child)
            # if up and till not returned
            adj[node] = []
            oder.append(node)
            done.add(node)

        for i in range(numCourses):
            if i in done: continue

            visit.clear()
            if back_edge(i):
                return []

        return oder

g = Solution()
#%%
# ans = [0, 1]
g.findOrder(numCourses = 2, prerequisites = [[1,0]])
# %%
# ans = [0,2,1,3]

g.findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])
# %%