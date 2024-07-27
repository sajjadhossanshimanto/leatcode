'''
https://leetcode.com/problems/daily-temperatures/description/
'''
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

#%%
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(temperatures)
        pos = len(temperatures)
        while temperatures:
            ele = temperatures.pop()
            pos -= 1
            while stack and ele>=stack[-1][0]:
                stack.pop()
            
            # finally we came to a position here `ele` is less than stac.top
            ans[pos] = stack[-1][1]-pos if stack else 0
            stack.append((ele, pos))
        
        return ans

s = Solution()
# %%
# [1,1,4,2,1,1,0,0]
s.dailyTemperatures([73,74,75,71,69,72,76,73])
# %%
# [1,1,1,0]
s.dailyTemperatures([30,40,50,60])
# %%
# [1,1,0]
s.dailyTemperatures([30,60,90])
# %%
