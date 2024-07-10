'''
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
'''
#%%
from typing import List
from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = defaultdict(list)
        rev_adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            rev_adj[b].append(a)
        
        def edge_counter(node, adj):
            visit.add(node)

            c = 0
            for child in adj[node]:
                if child in visit: continue
                
                C += edge_counter(child, adj) +1

            return c

        visit = set()
        ans, _ = edge_counter(0, adj)
        edge_counter(0, rev_adj)
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
