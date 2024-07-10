'''
https://leetcode.com/problems/redundant-connection/description/
'''
#%%
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        def find(a):
            if not a in parent:
                parent[a] = -1
                return a
            if parent[a]<0:
                return a
            r = find(parent[a])
            parent[a] = r
            return r
        
        def union(a, b):
            pa, pb = find(a), find(b)
            if abs(parent[pa])>abs(parent[pb]):
                parent[pb] = pa
                parent[pa] -=1
            else:
                parent[pa] = pb
                parent[pb] -=1

        for a, b in edges:
            if find(a)==find(b):
                return [a, b]
            
            union(a, b)


g = Solution()
#%%
# ans = [2, 3]
g.findRedundantConnection([[1,2],[1,3],[2,3]])
# %%
# ans = [1, 4]
g.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]])
# %%
