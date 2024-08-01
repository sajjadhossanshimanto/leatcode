'''
https://leetcode.com/problems/asteroid-collision/description/
- things to consider
- not every opsite sign num will collide
- 3, -1 will collide    --> <--
- but -1, 3 will not    <-- -->
'''
#%%
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []# proper varr name should be `right`
        for a in asteroids:
            # setting a=0 also prevents looping
            while stack and stack[-1]>0 and a<0:
                if -a == stack[-1]:
                    stack.pop()
                    a = 0
                elif -a>stack[-1]:
                    stack.pop()
                else:# a is small
                    # no append, no pop
                    a = 0
            
            if a: stack.append(a)

        return stack

s = Solution()
# %%
# ans = [5, 10]
s.asteroidCollision([5,10,-5])
#%%
# []
l = [8, -8]
#%%
# ans = [10]
s.asteroidCollision([10, 2, -5])
# %% wa 194
ans = [-2, -2, -2]
s.asteroidCollision([-2,-2,1,-2])
# %%
