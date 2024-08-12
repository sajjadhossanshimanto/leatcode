'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''
#%%
from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s): return []

        window = defaultdict(lambda :0)
        pattern = defaultdict(lambda :0)
        i=0# edge for while loop
        for i in range(len(p)):
            window[s[i]] += 1
            pattern[p[i]] += 1

        ans = [0] if window==pattern else []
        start = 0
        while i!=len(s)-1:
            # add
            i+=1
            window[s[i]] += 1

            # remove
            window[s[start]] -= 1
            if window[s[start]] == 0:
                window.pop(s[start])
            start += 1

            # check
            if pattern==window:
                ans.append(start)

        return ans

s = Solution()
#%%
# [0,6]
s.findAnagrams(s = "cbaebabacd", p = "abc")
#%%
# [0,1,2]
s.findAnagrams(s = "abab", p = "ab")
# %% error 2
# []
s.findAnagrams("aa", "bb")
# %%
# [1]
s.findAnagrams("baa", "aa")
# %% runtime error
s.findAnagrams("aa", "aaaaa")