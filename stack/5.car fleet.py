'''
https://leetcode.com/problems/car-fleet/submissions/1334777640/
'''
#%%
from typing import List


inf = float('inf')
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # return the number of car after fleet that will arrive at the distination
        c = 0
        min_time = None
        cars = sorted(
            zip(position, speed),
            key= lambda x: x[0]
        )
        # print(cars)
        for pos, speed in reversed(cars):
            time = (target-pos)/speed
            if not min_time:
                min_time = time
                # print("init min time", time)
            elif time<=min_time:
                # ager garir chay aro kom time modhe jete casce
                c+=1
                # print(time)
            elif time>min_time:
                # if this time is greater that means this one is more slower
                min_time = time
                # print("min time", time)

        return len(position)-c

s= Solution()
# %%
# ans = 3
s.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3])
# %%
# ans = 1
s.carFleet(target = 10, position = [3], speed = [3])
# %%
# ans = 1
s.carFleet(target = 100, position = [0,2,4], speed = [4,2,1])
# %%
