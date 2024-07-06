'''
https://leetcode.com/problems/parallel-courses-iii/description/
'''
#%%
from typing import List
from collections import defaultdict, deque
from heapq import heappop, heappush


inf = float('inf')
class Solution:
    def dfs(self, node):
        self.visit.add(node)
        if not self.adj[node]:
            return node

        for child in self.adj[node]:
            if child in self.visit: continue

            # self.root = 
            r=self.dfs(child)
        return r

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        self.visit = set()
        visit = self.visit
        self.root = 0
        
        self.adj = defaultdict(list)
        reverse_adj = defaultdict(list)
        for a, b in relations:
            a-=1
            b-=1
            self.adj[a].append(b)
            reverse_adj[b].append(a)
        
        self.root = self.dfs(self.root)

        # dijkstra
        q = []
        heappush(q, (0, self.root))# root, level
        
        self.visit.clear()
        visit.add(self.root)
        
        sssp = [-inf]*n
        sssp[self.root] = 0
        ans = 0
        while q:
            dis, node = heappop(q)
            dis = abs(dis)
            if dis<sssp[node]: continue

            if not reverse_adj[node]:
                sssp[node]+=time[node]
                ans = max(ans, abs(sssp[node]))
                continue
            
            for child in reverse_adj[node]:
                # if child in self.visit: continue
                # visit.add(child)

                nd = dis+time[node]# a bit strange here
                if nd<sssp[child]: continue

                sssp[child] = nd
                heappush(q, (-nd, child))

        return ans

g=Solution()
#%%
g.minimumTime(n = 3, relations = [[1,3],[2,3]], time = [3,2,5])
# %%
# ans = 12
# out = 9-----fixed
g.minimumTime(n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5])
#%%
g.root
# %%
