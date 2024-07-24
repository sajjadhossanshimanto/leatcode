
#%%
from typing import List
from itertools import combinations
from collections import Counter


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        c = Counter()
        for i in range(1, len(nums)):
            c.update(Counter(map(
                sum,
                combinations(nums, r=i)
            )))
            if k in c.values():
                return True

        return False


s = Solution()
# %%
s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], k=4)
# %%
