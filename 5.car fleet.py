
# see web
#%%
from typing import List


inf = float('inf')
class Solution:
    def carFleet(self, target:int,  position: List[int],  speed: List[int]) -> int:
        # return the number of car fleet that will arrive at the distination
        c = 0
        min_time = None
        position = sorted(
            [
                (position[i], i) for i in range(len(position))
            ],
            key= lambda x: x[0]
        )
        # for idx in range(len(position)-1, -1, -1):
        for pos, idx in position:
            time = (target-pos)/speed[idx]
            if not min_time:
                min_time = time
            elif time<=min_time:
                # ager garir chay aro kom time modhe jete casce
                c+=1
            elif time>min_time:
                min_time = time
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
