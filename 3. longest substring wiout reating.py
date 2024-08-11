'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
#%%
from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        ans = 0
        sub = set()
        for r in range(len(s)):
            if s[r] in sub:
                for l in range(l, r+1):
                    sub.remove(s[l])
                    if s[l]==s[r]:
                        l+=1
                        break
            
            sub.add(s[r])
            ans = max(ans, len(sub))
        
        return ans

s = Solution()
# %%
# 3
s.lengthOfLongestSubstring("abcabcbb")
# %%
# 1
s.lengthOfLongestSubstring("bbbbb")
# %%
# 3
s.lengthOfLongestSubstring("pwwkew")
# %%
