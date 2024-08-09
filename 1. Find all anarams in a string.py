'''
https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''
#%%
from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p = set(p)
        window = set()
        count = defaultdict(lambda :0)
        i=0
        for i in range(len(p)-1):
            window.add(s[i])
            count[s[i]] += 1

        ans = []
        while i!=len(s)-1:
            # add
            i+=1
            window.add(s[i])
            count[s[i]] += 1

            # check
            start = i-len(p)+1
            if p==window:
                ans.append(start)
            
            # remove
            count[s[start]]-=1
            if count[s[start]]==0:
                window.remove(s[start])
        
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
