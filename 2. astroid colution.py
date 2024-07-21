# see web
#%%
from typing import List


class Solution:
    def asteroidCollision(self, asteroids:List[int]) -> List[int]:
        def sign(num):
            if num<0: return -1
            return 1
        
        ans = []
        i = 0
        while i<n:
            a1 = asteroids[i]
            a2 = asteroids[i+1]
            if sign(a1) != sign(a2):
                if abs(a1)>abs(a2):
                    ans.append(a1)
                elif abs(a1)<abs(a2):
                    ans.append(a2)
            i+=1
        
        return ans