#%%
from typing import List


inf = float('inf')
class Solution:
    def largestRectngleArea(self, heights: List[int]) -> int:
        # heights = sorted(heights)# TODO: iterable sorter. i think its not possible until loop over all the ilement can't determin confirmly whitch one the max
        heights.sort()
        # TODO: list sort vs sorted time
        pop_count = 0
        ans = -inf
        while heights:
            h = heights.pop()
            pop_count += 1
            area = h*pop_count
            ans = max(ans, area)
        
        return ans

s = Solution()
# %%
s.largestRectngleArea([2, 1, 5, 6, 2, 3])
# %% random
s.largestRectngleArea([2, 1, 2, 3, 2])
# %%
