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
    def asteroidCollision(self, asteroids:List[int]) -> List[int]:
        def sign(num):
            if num<0: return -1
            return 1
        
        stack = []
        for a in asteroids:
            if stack and stack[0]>0 and a<0:
                a = -a# abs value
                if a == stack[-1]:
                    stack.pop()
                elif a>stack[-1]:
                    #TODO: this has to be iteratively
                    stack.pop()
                else:
                    # nothing to append
                    pass 
            else:
                stack.append(a)

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
