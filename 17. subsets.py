'''
https://leetcode.com/problems/subsets/submissions/1341623331/
'''
#%%
from typing import List
from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for ln in range(1, len(nums)):
            ans.extend(combinations(nums, r=ln))

        ans.append(nums)
        return ans

# %%
# [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# return type not nececeruly have tobe list[list], list[tupe] also ok
Solution().subsets([1, 2, 3])
# %%
Solution().subsets([0])
# %%
