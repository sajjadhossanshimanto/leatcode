'''
https://leetcode.com/problems/parallel-courses-iii/description/
'''
#%%
from typing import List
from collections import defaultdict, deque


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

    def bfs(self):
        pass

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
        self.visit.clear()

        q = deque()
        q.append((self.root, 1))# root, level
        visit.add(self.root)
        current_level = 1
        ans = 0
        _max = 0
        while q:
            node, level = q.popleft()
            if level!=current_level:
                # level has changed
                ans+=_max
                _max = 0
                current_level = level
            _max = max(_max, time[node])

            # if not reverse_adj:
            #     _max = max(_max, time[node])
                
            for child in reverse_adj[node]:
                if child in self.visit: continue
                visit.add(child)
                q.append((child, level+1))

        return ans+_max

g=Solution()
#%%
g.minimumTime(n = 3, relations = [[1,3],[2,3]], time = [3,2,5])
# %%
g.minimumTime(n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5])
#%%
g.root
# %%
