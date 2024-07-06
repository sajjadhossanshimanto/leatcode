'''
https://leetcode.com/problems/critical-connections-in-a-network/description/
'''
#%%
from typing import List
from collections import defaultdict


inf = float("inf")
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
        
        ans = []
        intime = [inf]*n
        lowtime = [inf]*n
        def dfs(node, parent, time):
            intime[node] = time
            lowtime[node] = time

            for child in adj[node]:
                if intime[child]!=inf:# if child in visit
                    # this child is not child actually an ansistor
                    if child!=parent:
                        lowtime[node] = min(lowtime[node], lowtime[child])
                        # TODO: here
                    continue

                time+=1
                dfs(child, node, time)
                lowtime[node] = min(lowtime[node], lowtime[child])
                if lowtime[child]>intime[node]:# low time of node might be lowered by previous line
                    ans.append([node, child])

        dfs(0, -1, 1)
        return ans

g=Solution()
#%%
g.criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]])
# %%
from test_helper import sample_test

sample_test(g.criticalConnections, "wa15", r"testcase\1.json")
# %%
