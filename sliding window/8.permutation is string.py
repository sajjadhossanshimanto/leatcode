'''
https://leetcode.com/problems/permutation-in-string/description/
- need O(n) algo
- as inpuut 10^4
'''
#%%
from typing import List


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 is pattern
        if len(s1) > len(s2): return False

        window = {}
        pattern = {}
        for i in range(len(s1)):
            pattern[s1[i]] = pattern.get(s1[i], 0) + 1
            window[s2[i]] = window.get(s2[i], 0) + 1

        if pattern==window: return True

        l = 0
        for r in range(len(s1), len(s2)):
            # add
            window[s2[r]] = window.get(s2[r], 0) + 1

            # remove
            window[s2[l]] -= 1
            if window[s2[l]]==0:
                window.pop(s2[l])
            l+=1
        
            # check
            if pattern==window: return True
        
        return False

s = Solution()
# %%
# ans = 1
s.checkInclusion(s1 = "ab", s2 = "eidbaooo")
# %%
# ans = 0
s.checkInclusion(s1 = "ab", s2 = "eidboaoo")
# %%
