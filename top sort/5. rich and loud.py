'''
https://leetcode.com/problems/loud-and-rich/description/
'''
#%%
from typing import List
from collections import defaultdict


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adj = defaultdict(list)
        for a, b in richer:
            # adj[a].append(b)
            adj[b].append(a)# according to the question
            # ans[1] -> 1 er opor jara tader mode k loud
        
        visit = [0]*len(quiet)
        def dfs(node):
            visit[node] = 1
            
            richer = node
            for child in adj[node]:
                if visit[child]:
                    r = ans[child]
                else:
                    r = dfs(child)

                if quiet[r]<quiet[richer]:# loud == less qukite
                    richer = r
            
            ans[node] = richer
            return richer

        ans = [-1]*len(quiet)
        for i in range(len(quiet)):
            if ans[i]!=-1: continue
            dfs(i)

        return ans

g = Solution()
#%%
# ans = [5,5,2,5,4,5,6,7]
g.loudAndRich(richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0])
#%%
g.loudAndRich
g.loudAndRich