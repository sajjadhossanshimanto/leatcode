'''
https://leetcode.com/problems/longest-repeating-character-replacement/description/
'''
#%%
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        max_len = 0
        max_count = 0
        l,r = 0, 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if window[s[r]] > max_count:
                max_count = window[s[r]]
            
            while (r-l+1) - max_count > k:
                window[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r-l+1)
        
        return max_len

s = Solution()
# %%
# 4
s.characterReplacement(s = "ABAB", k = 2)
# %%
# 4
s.characterReplacement( s = "AABABBA", k = 1)
# %% wa41
s.characterReplacement("BAAA", 0)
# %%
