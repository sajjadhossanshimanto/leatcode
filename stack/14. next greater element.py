'''
https://leetcode.com/problems/next-greater-element-i/description/
- 0-indexed
- arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`
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
        stack = []# of pos
        # while nums2:
        #     num = nums2.pop()
        # for num in (reversed(nums2)):
        # for pos in range(len(nums2)-1, -1, -1):
            # num = nums2[pos]
        for pos, num in reversed(nums2):
            if num not in index: continue

            while stack and num > nums2[stack[-1]]:
                pre_idx = stack.pop()
                ans[pre_idx] = idx - pre_idx