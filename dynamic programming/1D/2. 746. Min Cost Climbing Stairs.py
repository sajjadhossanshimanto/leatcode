# https://leetcode.com/problems/min-cost-climbing-stairs/
#%%
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] = (min(
                cost[i]+cost[i-1],
                cost[i]+cost[i-2]
            ))

        return min(cost[-1], cost[-2])
        # return min_cost
#%%
s = Solution()
s.minCostClimbingStairs([10,15,20])
# %%
s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
# %%
