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
        pre_sum = [k]
        
        for i in range(1, len(nums)+1):
            # i is 1 indexed. 
            # It is the devidor - index - count
            pre_sum.append(pre_sum[i-1] + nums[i-1])

            # at most k
            num = int(pre_sum[-1]/i)

        return i

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
