'''
https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
- nums length 10e5
- k = 10e5
- so need a O(n)
- return the frequency
'''
#%%
from typing import List


# who said the sum has to be from start to i
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        res, total = 0, 0
        l, r = 0, 0
        while r < len(nums):
            total += nums[r]
            
            # ulta condition
            while nums[r] * (r-l+1) > total+k:
                total -= nums[l]
                l+=1
            
            res = max(res, r-l+1)
            r += 1

        return res

s = Solution()
# %%
# 3
s.maxFrequency([1, 2,  4], 5)
# %%
# 2
s.maxFrequency(nums = [1,4,8,13], k = 5)
# %%
# 1
s.maxFrequency(nums = [3,9,6], k = 2)
# %%
