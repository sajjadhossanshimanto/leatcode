'''
https://leetcode.com/problems/network-delay-time/
'''
#%%
from typing import List
from collections import defaultdict
from heapq import heappush, heappop


inf = float("inf")

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for u, v, w in times:
            adj[u].append((v, w))
        
        node = k
        # def dijksta(node):
        sssp = [inf]*(n+1)
        sssp[node] = 0

        max_dis = 0
        visit = set()

        pq = []
        heappush(pq, (node, 0))
        while pq:
            node, dis = heappop(pq)
            visit.add(node)
            if dis>sssp[node]: continue
            for child, w in adj[node]:
                if w+dis>sssp[child]: continue
                sssp[child] = w+dis
                heappush(pq, (child, w+dis))
                max_dis = max(max_dis, w+dis)
        if len(visit)!=n: return -1
        return max_dis

#%%
Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)
# %%
Solution().networkDelayTime(times = [[1,2,1]], n = 2, k = 1)
# %%
Solution().networkDelayTime(times = [[1,2,1]], n = 2, k = 2)
#%%
Solution().networkDelayTime
Solution().networkDelayTime