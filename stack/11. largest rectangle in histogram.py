#%%
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []
        for idx, h in enumerate(heights):
            start = idx
            while stack and h < heights[stack[-1]]:
                r = stack.pop()
                area = max(
                    area,
                    heights[r]*(idx-r)
                )
                start = r
            stack.append(start)# most importantthing
            # currentheight is less so the weight should include poped indixes
        
        
        return area

s = Solution()
# %%
# ans = 10
s.largestRectangleArea([2, 1, 5, 6, 2, 3])
# %% random
s.largestRectangleArea([2, 1, 2, 3, 2])
# %%
# ans = 4
s.largestRectangleArea([2, 4])
# %%
# ans = 2
# out = 4
s.largestRectangleArea([2,0,2])
# %% wa 2
s.largestRectangleArea([0])
# %%
