'''
https://leetcode.com/problems/min-cost-to-connect-all-points/
'''
#%%
from typing import List
from heapq import heappush, heappop


class Solution:
    def find(self, pos:tuple[int, int]):
        # pos = (x, y)
        if pos not in self.parents:
            self.parents[pos] = 1
            return pos
        
        if isinstance(self.parents[pos], int):
            return pos
        
        r = self.find(self.parents[pos])
        self.parents[pos] = r
        return r

    def union(self, pos1:tuple[int, int], pos2:tuple[int, int]):
        ''' 
        - it is confirmed that parent[pos1]!=parent[pos2]
        - 
        '''
        p1 = self.parents[self.find(pos1)]
        p2 = self.parents[self.find(pos2)]
        if p1>=p2:
            # make pos1 as parent
            self.parents[self.find(pos1)]=p1+p2
            self.parents[self.find(pos2)] = self.find(pos1)
        else:
            self.parents[self.find(pos2)]=p1+p2
            self.parents[self.find(pos1)] = self.find(pos2)


    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.parents = {}
        ans = 0
        pq = []

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                val = abs(x1-x2)+abs(y1-y2)
                heappush(pq, (val, (x1, y1), (x2, y2)))

        i=0
        while i!=len(points)-1:
            w, pos1, pos2 = heappop(pq)
            if self.find(pos1)==self.find(pos2):
                continue
            # print(w, pos1, pos2)
            i+=1
            ans+=w
            self.union(pos1, pos2)

        return ans

g = Solution()
#%%
# ans = 18
g.minCostConnectPoints(points = [[3,12],[-2,5],[-4,1]])
# %%
# ans = 20
# out = 11
g.minCostConnectPoints(points = [[0,0],[2,2],[3,10],[5,2],[7,0]])
# %%
