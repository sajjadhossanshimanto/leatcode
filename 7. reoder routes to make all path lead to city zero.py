'''
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
'''
#%%
from typing import List
from collections import defaultdict, deque


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        parent = {}
        def find(a):
            if a not in parent:
                parent[a] = -1
                return a
            if parent[a]<0:
                return a

            r = find(parent[a])
            parent[a] = r
            return r

        def union(a, b):
            p1 = find(a)
            p2 = find(b)
            parent[p2] = p1
            parent[p1] -=1

        ans = 0
        connections = deque(connections)
        while connections:# or while len(0)!=n
            a, b = connections.popleft()
            # a ---> b
            # if b point to 0: right edge
            if find(b)==0:
                union(a, b)
            elif find(a)==0:
                ans+=1
                union(b, a)
            else:
                connections.append((a, b))
        
        return ans

g = Solution()
#%%
# ans = 3
g.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]])
# %%
