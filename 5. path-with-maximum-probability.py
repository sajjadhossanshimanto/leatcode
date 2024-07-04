'''
https://leetcode.com/problems/path-with-maximum-probability/description/
- zero indexed
- for n nodes its not gurantd there would be n edges
'''
#%%
from typing import List
from collections import deque, defaultdict
from heapq import heappush, heappop


inf = float("inf")
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = defaultdict(list)

        succProb = iter(succProb)
        for a, b in edges:
            w = next(succProb)
            adj[a].append((b, w))
            adj[b].append((a, w))

        # def dijkstra():
        sssp=[inf]*n
        sssp[start]=0
        pq = []
        heappush(pq, (1, start))

        while pq:
            dis, node = heappop(pq)
            if node in visit or dis>sssp[node]: continue
        
            for child, w in adj[node]:
                nd = w+dis
                if nd>sssp[child]: continue
                sssp[child] = nd
                heappush(pq, (nd, child))

        return 

#%%
Solution().maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2)
#%%
# ex = .3
Solution().maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2)
#%%
Solution().maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2)
#%%
Solution().maxProbability
Solution().maxProbability
Solution().maxProbability