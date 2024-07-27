
# see web
#%%
from typing import List


inf = float('inf')
class Solution:
    def carFleet(self, target:int,  position: List[int],  speed: List[int]) -> int:
        # return the number of car fleet that will arrive at the distination
        c = 0
        min_time = None
        cars = sorted(
            zip(position, speed),
            key= lambda x: x[0]
        )
        print(cars)
        # for idx in range(len(position)-1, -1, -1):
        for pos, speed in reversed(cars):
            time = (target-pos)/speed
            if not min_time:
                min_time = time
                print("min time", time)
            elif time<=min_time:
                # ager garir chay aro kom time modhe jete casce
                c+=1
                print(time)
            elif time>min_time:
                min_time = time
                print("min time", time)
            # min_time = max(min_time, )

        return c

s= Solution()
# %%
# ans = 3
s.carFleet(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3])
# %%
l=[1, 2, 3, 4]
reversed(l)
# %%
