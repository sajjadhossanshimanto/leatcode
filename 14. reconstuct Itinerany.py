'''
https://leetcode.com/problems/reconstruct-itinerary/description/
- every question has a context. understanding the background is very importent
- whitch i don't reach catch by myself in this question
'''
#%%
from typing import List
from collections import defaultdict


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for a, b in tickets:
            adj[a].append(b)
        
        for a in adj:
            adj[a].sort(reverse=True)

        edge = defaultdict(lambda :defaultdict(lambda :0))
        result = []
        def dfs(node):
            result.append(node)
            if len(result) == len(tickets)+1:
                return True

            for _ in range(len(adj[node])):
                # if not adj[node] loopwould auto refuse
                child = adj[node].pop()
                if dfs(child): return True
                adj[node].insert(0, child)
                result.pop()# pop child

            return False

        dfs("JFK")
        return result

s = Solution()
# %%
# ["JFK","MUC","LHR","SFO","SJC"]
s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])
# %%
# ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
s.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
# %%
# ans = ["JFK","NRT","JFK","KUL"]
# out = ["JFK","KUL","NRT","JFK"]
s.findItinerary([["JFK","KUL"], ["JFK","NRT"], ["NRT","JFK"]])
# edge case: we have to finish a sucessfull loop
# j is connected to k
# j is connected to n
# but from j if we go to k first we got stuck. k is not connected to n

# %% wa8
# ans = ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","JFK"]
# out = ["JFk"]
s.findItinerary([["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["TIA","JFK"],["ANU","TIA"],["JFK","TIA"]])
# %%
