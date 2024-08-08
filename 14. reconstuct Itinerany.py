'''
- every question has a context. understanding the background is very importent
- whitch i don't reach catch by myself in this question
'''
#%%
from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for a, b in tickets:
            adj[a].append(b)
        n = len(adj)

        edge = [[0]*n for _ in range(n)]
        result = []
        def dfs(node):
            result.append(node)

            for child in adj[node]:
                if edge[node][child]: continue

                dfs(node)

        dfs("JFK")# TODO: smallest lexical order
        return result

s = Solution()
# %%
s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
# %%
