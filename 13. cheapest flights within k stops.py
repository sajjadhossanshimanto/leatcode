'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/
'''
#%%
from typing import List
from collections import defaultdict
from heapq import heappush, heappop


inf = float("inf")
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for a, b, w in flights:
            adj[a].append((b, w))
        
        visit = [0]*n
        sssp = [inf]*n
        sssp[src] = 0

        q = []
        heappush(q, (0, src, k))# dis, node, step_count
        while q:
            dis, node, step = heappop(q)
            if dis>sssp[node]: continue
            if node==dst:
                # excluding the dist node from counting
                print(step, "-->", dis)
                if step-1<=k:
                    return dst
            
            for child, w in adj[node]:
                if visit[child]: continue
                if child!=dst:
                    visit[child]=1

                nd = dis+w
                if nd<sssp[child]:
                    sssp[child]=nd
                    heappush(q, (nd, child, step+1))
        return -1

g = Solution()
#%%
# ans = 700
g.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1)
# %%
# ans 500
g.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1)
# %%
