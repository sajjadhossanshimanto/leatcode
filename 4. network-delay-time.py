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

        visit = set()
        max_time = node# never possible as sssp[node] is set to zero

        pq = []
        heappush(pq, (0, node))
        while pq:
            dis, node = heappop(pq)
            if dis>sssp[node]or node in visit: continue
            visit.add(node)

            if sssp[node]>sssp[max_time]: 
                max_time = node

            for child, w in adj[node]:
                nd = w+dis
                if nd>sssp[child]: continue
                sssp[child] = nd
                heappush(pq, (nd, child))

        if len(visit)!=n or max_time==k: return -1
        return sssp[max_time]

#%%
Solution().networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2)
# ex = 2
# %%
Solution().networkDelayTime(times = [[1,2,1]], n = 2, k = 1)
# ans = 1
# %%
Solution().networkDelayTime(times = [[1,2,1]], n = 2, k = 2)
# ans = -1
#%%
Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,4]], n=3, k=1)
# ex = 3
# out = 4--resolved
#%% time limit
from test_helper import sample_test

sample_test(Solution().networkDelayTime, "39tl", r"testcase\4.json")
# use 
# bfs to levelel graph
# dfs to go to the firthest
#%%
Solution().networkDelayTime
Solution().networkDelayTime