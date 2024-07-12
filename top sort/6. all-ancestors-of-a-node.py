'''
https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/description/
'''
#%%
from typing import List
from collections import defaultdict
from itertools import chain


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for a, b in edges:
            # adj[a].append(b)
            adj[b].append(a)

        visit = [0]*n
        def dfs(node):
            visit[node]=1

            ansistor = []
            for child in adj[node]:
                if visit[child]:
                    r = ans[child]
                else:
                    r = dfs(child)
                # r = r.copy()
                ansistor = chain(ansistor, [child], r)
                # ansistor = ansistor+[child]+r
            
            ans[node] = sorted(set(ansistor))
            # print(node, ans[node])
            return ans[node]

        ans = [[] for _ in range(n)]
        for i in range(n):
            if not visit[i]:
                dfs(i)
        
        return ans


g = Solution()
#%%
# ans = [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
g.getAncestors(n = 8, edges = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]])
# %%
