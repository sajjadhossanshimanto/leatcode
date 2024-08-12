'''
https://leetcode.com/problems/sliding-window-maximum/
'''
#%%
from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        stack = deque()
        l=0
        # preparing window
        for r in range(k):
            while stack and nums[r] >= nums[stack[-1]]:
                stack.pop()
            stack.append(r)

        ans.append(nums[stack[0]])
        for r in range(r+1, len(nums)):
            # remove l
            if stack[0]==l:
                stack.popleft()
            l+=1
            
            # increase r
            while stack and nums[r] >= nums[stack[-1]]:
                stack.pop()
            stack.append(r)

            # calculate            
            ans.append(nums[stack[0]])

        return ans

s = Solution()
# %%
# [3,3,5,5,6,7]
s.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3)
# %%
s.maxSlidingWindow([1], 1)
# %%
