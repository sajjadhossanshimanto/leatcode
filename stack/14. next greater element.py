'''
https://leetcode.com/problems/next-greater-element-i/description/
- 0-indexed
- `nums1` is a subset of `nums2`
- All integers in `nums1` and `nums2` are unique
- build  O(nums1.length + nums2.length) solution
'''
#%%
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index = {}
        for pos, num in enumerate(nums1):
            index[num] = pos
        
        ans = [-1]*len(nums1)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                pre = stack.pop()
                if pre in index:
                    ans[index[pre]] = num
            stack.append(num)

        return ans

s = Solution()
# %%
# ans = [-1, 3, -1]
s.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2])
# %%
# ans = [3, -1]
s.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4])
# %%
