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
