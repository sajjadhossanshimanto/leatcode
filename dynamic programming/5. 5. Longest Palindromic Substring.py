# https://leetcode.com/problems/longest-palindromic-substring/

#%%
class Solution:
    def longestPalindrome(self, s: str) -> str:
        mxln = 0
        mxpal = ""
        for i in range(len(s)):
            l = r = i
            while l>0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            ln = r-l+1
            # print(s[l:r+1])
            if ln>mxln:
                mxpal = s[l:r+1]
                mxln = ln
        
        return mxpal

#%%
s = Solution()
s.longestPalindrome("babad")
# %%
s.longestPalindrome("cbbd")
# %%
