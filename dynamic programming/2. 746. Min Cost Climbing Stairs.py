# https://leetcode.com/problems/min-cost-climbing-stairs/
#%%
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            min_cost.append(min(
                cost[i]+min_cost[i-1],
                cost[i]+min_cost[i-2]
            ))

        return min(min_cost[-1], min_cost[-2])
        # return min_cost
#%%
s = Solution()
s.minCostClimbingStairs([10,15,20])
# %%
s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
# %%
