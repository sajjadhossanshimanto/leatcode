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

        # return n, start, end
        succProb = iter(succProb)
        for a, b in edges:
            w = next(succProb)
            adj[a].append((b, w))
            adj[b].append((a, w))

        # def dijkstra():
        sssp=[0.0]*n
        sssp[start]=-1
        pq = []
        heappush(pq, (-1, start))
        visit = set()

        while pq:
            dis, node = heappop(pq)
            if node in visit or dis>sssp[node]: continue
            visit.add(node)

            for child, w in adj[node]:
                nd = -abs(w*dis)
                if nd>sssp[child]: continue
                
                sssp[child] = nd
                if node!=end:
                    heappush(pq, (nd, child))

        return abs(sssp[end])

#%%
Solution().maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2)
# ans =.25
#%%
# ex = .3
Solution().maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2)
#%%
Solution().maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2)
# ans = 0.0
#%% wrong ans
# ex = 0.34414
# out = 0.02214
from test_helper import sample_test

sample_test(Solution().maxProbability, "d", r"testcase\5.json")

#%%
Solution().maxProbability
Solution().maxProbability
#%%
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
                # Create the adjacency list
        adj_list = [{} for _ in range(n)]
        for i in range(len(edges)):
            a, b = edges[i]
            adj_list[a][b] = succProb[i]
            adj_list[b][a] = succProb[i]  # Since the graph is undirected

        # Priority queue
        maxHeap = []
        heappush(maxHeap, (-1, start_node))  # Using -1 to simulate max-heap with min-heap

        # Dictionary to store the maximum probability to each node
        probabilities = [0.0] * n
        probabilities[start_node] = 1.0

        while maxHeap:
            probability, node = heappop(maxHeap)
            probability = -probability  # Convert back to positive

            if node == end_node:
                return probability

            for neighbor, edge_prob in adj_list[node].items():
                new_prob = probability * edge_prob
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heappush(maxHeap, (-new_prob, neighbor))  # Push negative to simulate max-heap

        return 0.0