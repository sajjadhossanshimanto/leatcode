'''
https://leetcode.com/problems/asteroid-collision/description/
'''
#%%
from typing import List


class Solution:
    def asteroidCollision(self, asteroids:List[int]) -> List[int]:
        def sign(num):
            if num<0: return -1
            return 1
        
        ans = []
        for next_ in asteroids:
            if not ans: ans.append(next_)
            else:
                if sign(next_) != sign(ans[-1]):
                    prev = ans.pop()
                    if abs(next_)==abs(prev):
                        # no append 
                        continue
                    if abs(next_)>abs(prev):
                        ans.append(next_)
                    else:
                        ans.append(prev)
                else:
                    ans.append(next_)
        
        return ans

s = Solution()
# %%
# ans = [5, 10]
l = [5,10,-5]
#%%
# []
l = [8, -8]
#%%
ans = [10]
l = [10, 2, -5]
#%%
s.asteroidCollision(l)
# %%
