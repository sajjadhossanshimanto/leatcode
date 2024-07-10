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
            '''return newly added child count'''
            p1 = find(a)
            p2 = find(b)
            parent[p2] = p1
            parent[p1] += parent[p2]
            return abs(parent[p1])

        def union_rank(a, b):
            '''return newly added child count'''
            p1 = find(a)
            p2 = find(b)
            if parent[p1]>parent[p2]:
                parent[p2] = p1
                parent[p1] += parent[p2]
            else:
                parent[p1] = p2
                parent[p2] += parent[p1]

        ans = 0
        connections = deque(connections)
        while connections:# or while len(0)!=n
            a, b = connections.popleft()
            # a ---> b
            # if b point to 0: right edge
            if find(b)==0:
                # as b tends to zero
                union(b, a)
            elif find(a)==0:
                ans+=union(a, b)
            else:
                union_rank((a, b))
        return ans

g = Solution()
#%%
# ans = 3
g.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]])
# %%
