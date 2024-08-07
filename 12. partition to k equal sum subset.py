'''
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
'''
#%%
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n<k: return False

        target, remin = divmod(sum(nums), k)# O(n)
        if remin: return False

        if max(nums)>target: return False

        visit = [0]*n
        def backtrack(i, k, pre_sum):
            if k==0:
                return True
            if pre_sum==target:
                # start checking from zero 
                return backtrack(0, k-1, 0)

            # starting from i
            for i in range(i, n):
                if visit[i] or nums[i] + pre_sum > target: continue

                visit[i] = 1
                if backtrack(i+1, k, pre_sum + nums[i]):
                    return True
                visit[i] = 0
            
            return False

        return backtrack(0, k, 0)

s = Solution()
# %%
# 1
s.canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], k=4)
# %%
# 0
s.canPartitionKSubsets([1,2,3,4], k=3)
# %%
