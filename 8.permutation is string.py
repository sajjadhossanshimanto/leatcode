'''
https://leetcode.com/problems/permutation-in-string/description/
'''
#%%
from typing import List
from itertools import permutations

#%%
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s1 is pattern
        if len(s1) > len(s2): return False

        set1 = set()
        l = 0
        r = len(s1)
        while r<=len(s2):
            set1.add(s2[l:r])
            l+=1
            r+=1
        
        for i in permutations(s1):
            if "".join(i) in set1: return True
        
        return False

s = Solution()
# %%
# ans = 1
s.checkInclusion(s1 = "ab", s2 = "eidbaooo")
# %%
# ans = 0
s.checkInclusion(s1 = "ab", s2 = "eidboaoo")
# %%
