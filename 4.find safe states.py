'''
https://leetcode.com/problems/find-eventual-safe-states/description/
'''
#%%
from typing import List


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        visit = set()
        def dfs(node):
            print(node)
            visit.add(node)
            # if not graph[node]:
            #     ans.append(node)
            #     return True

            safe = True
            for child in graph[node]:
                if child in visit:
                    continue

                if not dfs(child):
                    safe = False
            
            if safe:
                ans.append(node)
                print('append', node)
                return True

        ans = []
        for i in range(len(graph)):
            if i in visit: continue
            dfs(i)
        
        # ans.sort()
        return ans

g = Solution()
#%%
#  ans = [2, 4, 5, 6]
g.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])
# %%
