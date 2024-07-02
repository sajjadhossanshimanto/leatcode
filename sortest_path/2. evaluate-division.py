''' url = https://leetcode.com/problems/evaluate-division/description/
'''
#%%
from typing import List
from collections import defaultdict

class Solution:
    def dfs(self, a, b):
        self.visit.add(a)
        for child, w in self.adj[a]:
            if child in self.visit: continue
            
            if self.res is None: self.res = w
            else: self.res*=w
            
            if child==b: return
            self.dfs(child, b)

    def find(self, a):
        if a not in self.parent:
            self.parent[a] = 1
            return a
        
        if isinstance(self.parent[a], int): return a
        p = self.find(self.parent[a])
        self.parent[a] = p
        return p
    
    def union(self, a, b):
        if self.find(a)==self.find(b): return
        # no need to check for who is larger parent. as edge is directed
        self.parent[self.find(b)] = self.find(a)

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        self.adj = defaultdict(list)
        self.parent = {}

        # prepare adj
        for i in range(len(values)):
            a, b = equations[i]
            w = values[i]
            self.adj[a].append([b, w])
            self.adj[b].append([a, 1/w])

            self.union(a, b)

        ans = []
        for a, b in queries:
            if self.find(a)!=self.find(b):
                ans.append(-1.0)
                continue

            self.visit = set()
            self.res = None
            if self.res is None: ans.append(-1.0)
            else: ans.append(self.res)

        return ans
# %%
g=Solution().calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]])
g
# %%
