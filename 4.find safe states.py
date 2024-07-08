'''
https://leetcode.com/problems/find-eventual-safe-states/description/
'''
#%%
from typing import List
# from heapq import heappop, heappush


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        visit = set()
        def dfs(node):
            # print(node)
            visit.add(node)

            safe = True
            for child in graph[node]:
                if child in visit:
                    safe = False
                    continue
                
                if child in done: continue
                if not dfs(child):
                    safe = False
            
            if safe:
                # heappush(ans, node)
                ans.append(node)
                print('append', node)
                visit.remove(node)
                done.add(node)
                return True

        ans = []
        done = set()
        for i in range(len(graph)):
            if i in visit or i in done: continue
            dfs(i)
        
        ans.sort()
        return ans

g = Solution()
#%%
#  ans = [2, 4, 5, 6]
g.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])
# %% tl111
from test_helper import sample_test

sample_test(g.eventualSafeNodes, 'tl111', r"testcase\4.json")
# %%
