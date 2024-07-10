'''
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
'''
#%%
from typing import List
from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
        
        visit = set()
        def dfs(node):
            visit.add(node)

            c = 0
            fold = False
            for child in adj[node]:
                if child in visit: continue
                
                if child==0:
                    fold = True
                else:
                    r, fold = dfs(child)
                    c+=r

            return c, fold

        ans = 0
        for i in range(n):
            if i not in visit:
                c, fold = dfs(i)
                if fold: ans+=c

        return ans

g = Solution()
#%%
# ans = 3
g.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]])
# %%
