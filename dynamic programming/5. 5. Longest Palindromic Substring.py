# https://leetcode.com/problems/longest-palindromic-substring/

#%%
class Solution:
    def longestPalindrome(self, s: str) -> str:
        mxln = 0
        mxpal = ""
        for i in range(len(s)):
            
            # odd
            l = r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                ln = r-l+1
                # print(s[l:r+1])
                if ln>mxln:
                    mxpal = s[l:r+1]
                    mxln = ln
                
                l-=1
                r+=1

            # even
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                ln = r-l+1
                if ln>mxln:
                    mxpal = s[l:r+1]
                    mxln = ln
                
                l-=1
                r+=1

        return mxpal

#%%
s = Solution()
s.longestPalindrome("babad")
# %%
s.longestPalindrome("cbbd")
# %%
