'''
https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
'''
#%%
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        max_count = 0
        ans = None
        pre_sum = []
        counter = {}
        for i in range(len(nums)):
            if i>0:
                pre_sum.append(pre_sum[i-1] + nums[i])
            else:
                pre_sum.append(nums[i])
            counter[i] = counter.get(i, 0) + 1
            
            # at most k
            for j in range(k):
                div, mod = divmod((pre_sum[-1]+j), (i+1))
                if mod == 0:
                    #TODO: should i include if div not in counter
                    counter[div] = counter.get(div, 0) + (i+1)
                    if counter[div]>max_count:
                        ans = div
                        max_count = counter[div]
        
        return ans

s = Solution()
# %%
# 4
s.maxFrequency([1, 2,  4], 5)
# %%
