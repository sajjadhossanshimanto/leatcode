'''
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/
- sol: https://www.youtube.com/watch?v=m17yOR5_PpI&list=PLot-Xpze53ldBT_7QA8NVot219jFNr_GI&index=11
'''
#%%
from typing import List
from collections import defaultdict, deque


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {}
        adj = defaultdict(list)
        edge = set()
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
            edge.add((a, b))
        del connections
        
        ans = [0]
        visit = set()
        def dfs(node):
            visit.add(node)

            for child in adj[node]:
                if child not in visit:
                    if (node, child) in edge:
                        ans[0]+=1
                    dfs(child)

        dfs(0)
        return ans[0]

g = Solution()
#%%
# ans = 3
g.minReorder(n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]])
# %% tl75/76
from test_helper import sample_test
import sys

sys.setrecursionlimit(50000)

sample_test(g.minReorder, 'tl75', r'testcase\7.json')
# %%
