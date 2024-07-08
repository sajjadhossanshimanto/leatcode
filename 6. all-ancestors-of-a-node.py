'''
https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/
'''
#%%
from typing import List
from collections import defaultdict
from itertools import chain


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)

        visit = set()
        def dfs(node):
            visit.add(node)

            ansistor = []
            for child in adj[node]:
                if child in visit:
                    r = ans[child]
                else:
                    r = dfs(child)
                ansistor = chain(ansistor, r)
            
            ans[node] = sorted(ansistor)
            return ans[node]

        ans = [[] for _ in range(n)]
        for i in range(n):
            if i in visit: continue
            dfs(i)
        
        return ans


g = Solution()
#%%
g.getAncestors(n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]])
# %%
