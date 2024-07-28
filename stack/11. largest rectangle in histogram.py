#%%
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = []
        for idx, h in enumerate(heights):
            start = idx
            while stack and h <  stack[-1][1]:
                top_idx, top_h = stack.pop()
                area = max(
                    area,
                    top_h*(idx-top_idx)
                )
                start = top_idx
            stack.append((start, h))# most importantthing
            # currentheight is less so the weight should include poped indixes
        
        # some index goes to the end
        for i, h in stack:
            area = max(area, h * (len(heights)-i))
        
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
