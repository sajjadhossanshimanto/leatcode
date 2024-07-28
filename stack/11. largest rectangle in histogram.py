#%%
from typing import List
from heapq import heappush, heappop


inf = float('inf')
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        hlist = [[]]
        pointer = hlist[-1]
        for i in heights:
            if i==0:
                hlist.append([])
                pointer = hlist[-1]
            else:
                heappush(pointer, -i)

        ans = -inf
        while heights:
            h = heights.pop()
            pop_count += 1
            area = h*pop_count
            ans = max(ans, area)
        
        return ans

s = Solution()
# %%
s.largestRectangleArea([2, 1, 5, 6, 2, 3])
# %% random
s.largestRectangleArea([2, 1, 2, 3, 2])
# %%
# ans = 4
s.largestRectangleArea([2, 4])
# %%
ans = 2
out = 4
s.largestRectangleArea([2,0,2])