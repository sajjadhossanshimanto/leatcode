# https://leetcode.com/problems/palindromic-substrings/description/

#%%
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            
            # odd
            l = r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1
                
                l-=1
                r+=1

            # even
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                count+=1

                l-=1
                r+=1

        return count

#%%
s = Solution()
s.longestPalindrome("abc")
# %%
s.longestPalindrome("aaa")
# %%
