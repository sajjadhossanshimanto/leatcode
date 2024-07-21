# see web
# see if is enmerate slow
#%%
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        for i in  range(len(temperatures)):
            temp1= temperatures[i]
            for j in range(i+1, j):
                temp2= temperatures[j]
                if temp2>temp1:
                    ans[i] = j-i+1
        
        return ans

#%%
from heapq import heappush, heappop

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        sol = []# list of tuple(num, idx)
        for pos, temp in enumerate(temperatures):
            if sol:
                while temp>=sol[0][0]:# TODO: is't it always the 1st element
                    min_tem, min_pos = heappop(sol)
                    ans[min_pos] = min_pos-pos+1# TODO: +! may not rewquired

            heappush(sol, (temp, pos))