'''
https://leetcode.com/problems/find-edges-in-shortest-paths/description/
- graph may not be connected
'''
#%%
from typing import List
from collections import defaultdict
from heapq import heappop, heappush


inf = float("inf")
class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        i=0
        for a, b, w in edges:
            adj[a].append((b, w, i))
            adj[b].append((a, w, i))
            i+=1

        ans = [False]*len(edges)
        ans[0] = True
        # ans[-1] = True# graph may not be connected
        reached_end = False

        # def dijkstra(node):
        pq = []
        heappush(pq, (0, 0))
        # visit = set()
        sssp = [inf]*n
        parents = {}
        while pq:
            dis, node = heappop(pq)
            if dis>sssp[node]:# node `eq` used
                continue
            if node==(n-1):
                # min_dis = #TODO do i need that
                reached_end = True

            for child, w, i in adj[node]:
                nd = dis+w
                if nd>sssp[child]:
                    continue
                
                sssp[child]=nd
                ans[i]=True
                heappush(pq, (nd, child))

        if not reached_end: return [False]*len(edges)
        return ans

g= Solution()
# %%
g.findAnswer(n = 6, edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]])
# %%
