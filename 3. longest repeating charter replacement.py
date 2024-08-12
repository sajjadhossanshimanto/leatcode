'''
https://leetcode.com/problems/longest-repeating-character-replacement/description/
'''
#%%
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        max_len = 0
        max_count = ("$", 0)# (k, v)
        l,r = 0, 0
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            if window[s[r]] > max_count[1]:
                max_count = [s[r], window[s[r]]]
            
            # ln_window = r-l+1
            while (r-l+1) - max_count[1] > k:
                if s[l] == max_count[0]:
                    max_count[1] -= 1
                window[s[l]] -= 1
                # TODO: do i need to remove if 0
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
# %%
