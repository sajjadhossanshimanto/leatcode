'''
https://leetcode.com/problems/path-with-maximum-probability/description/
- zero indexed
'''
#%%
from typing import List
from collections import deque, defaultdict


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(list)

        for i in range(n):
            a, b = edges[i]
            w = succProb[i]
            adj[a].append((b, w))
            adj[b].append((a, w))
        
        visit = set()

        def dfs(node, cost=1):
            visit.add(node)
            for child, w in adj[node]:
                if child in visit: continue
                
                # avoid marking end_point as visit
                # so that alternative paths can reach that node as well
                if child==end: return cost*w
                r = dfs(child, cost*w) or 0
                if r>max_dis[0]: max_dis[0] = r

        max_dis = [0.0]
        dfs(start)
        return max_dis[0]

#%%
Solution().maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2)
#%%
Solution().maxProbability
Solution().maxProbability