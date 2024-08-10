'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''
#%%
from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mod = 10000000
        base = 26
        m = len(p)
        def hash_string(s):
            h = 0
            for i in range(m):
                h += ord(s[i])*pow(base, m-i-1, mod)
            return h
        phash = hash_string(p)

        window = 0
        for i in range(len(p)-1):
            window += ord(s[i])*pow(base, m-i-1, mod)

        ans = []
        while i!=len(s)-1:
            # add
            i+=1
            window += ord(s[i])# * base power 0

            # check
            if phash==window:
                ans.append(start)
            
            # remove
            start = i-m+1
            window -= ord(s[start])*pow(base, m-1, mod)
            window *= 10

        return ans

s = Solution()
#%%
# [0,6]
s.findAnagrams(s = "cbaebabacd", p = "abc")
#%%
# [0,1,2]
s.findAnagrams(s = "abab", p = "ab")
# %% error 2
s.findAnagrams("aa", "bb")
# %%
