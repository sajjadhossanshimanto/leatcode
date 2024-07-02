'''
https://leetcode.com/problems/path-with-maximum-probability/description/
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
        q = deque()# (node,  dis_sum)
        q.append((start, 0))
        max_dis = 0.0# refalut ans is 0.00000
        while q:
            node, dis = q.popleft()
            if node == end:
                if dis>max_dis: max_dis = dis
                # continue

            for child, w in adj[node]:
                if child in visit: continue
                
                visit.add(child)
                q.append((child, dis+w))
        
        return max_dis
