#%%
from typing import List
from itertools import combinations


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = tuple(nums)
        ans = {tuple()}
        for ln in range(1, len(nums)):
            ans.update(
                map(
                    tuple, # list not hashible
                    map(# hash varies depending element pos (1, 4) & (4, 1) is diff
                        sorted, combinations(nums, r=ln)
                    )
                )
            )

        ans.add(nums)
        return ans

# %%
Solution().subsetsWithDup([1, 2, 3])
# %%
Solution().subsetsWithDup([1, 2, 2])
# %%
Solution().subsetsWithDup([0])
# %% wa 15
# ans = [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
# out = [[],[1],[4,4],[4,4,1,4],[4,4,4,4],[4,1,4],[4,4,1],[4],[1,4],[4,4,4],[4,4,4,1,4],[4,1],[4,4,4,1]]
Solution().subsetsWithDup([4,4,4,1,4])
# %%
