'''
https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/description/
'''
#%%
from typing import List
from collections import deque


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        def bfs(node, money):
            visit = set()
            visit.add(node)
            q = deque()
            q.append((node, money))
            c = 0
            while q:
                node, money = q.popleft()
                for child, w in adj[node]:
                    if child in visit: continue
                    visit.add(node)
                    if w>money: 
                        continue
                    c+=1
                    if money==w: continue# no more traversal needed
                    q.append((child, money-w))
            return c

        adj = [[] for _ in range(n)]
        for a, b, w in edges:
            adj[a].append((b, w))
            adj[b].append((a, w))

        min_nei = float('inf')
        min_node = -1
        for i in range(n):
            neiber = bfs(i, distanceThreshold)
            if neiber==min_nei:
                if i>min_node: min_node = i
            elif neiber<min_nei:
                min_nei = neiber
                min_node = i
        
        return min_node
#%%
Solution().findTheCity(n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4)
# ans = 3
# %%
Solution().findTheCity(n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2)
# ex = 0
# out = 4
# %%
