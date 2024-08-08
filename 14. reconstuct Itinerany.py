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

        edge = defaultdict(lambda :defaultdict(lambda :0))
        result = []
        def dfs(node):
            result.append(node)

            for child in adj[node]:
                if edge[node][child]: continue

                edge[node][child] = 1
                dfs(child)

        dfs("JFK")# TODO: smallest lexical order
        return result

s = Solution()
# %%
# ["JFK","MUC","LHR","SFO","SJC"]
s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
# %%
# ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
# %%
