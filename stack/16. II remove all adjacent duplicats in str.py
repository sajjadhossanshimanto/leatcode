'''
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
'''
#%%
#  this is actully  Counter data class 
#  except it's like a dict that supports one multiple time 
#  stupid thought but worth it
class Solution:
    def removeDuplicates(self, s: str, k: int) -> int:
        counter = []
        for char in s:
            if counter and counter[-1][0]==char:
                counter[-1][1] += 1
            else:
                counter.append([char, 1])

            if counter[-1][1]==k:
                counter.pop()

        return "".join(i*c for i, c in counter)

s = Solution()
# %%
# ans = "abcd"
s.removeDuplicates(s = "abcd", k = 2)
# %%
# ans = "aa"
s.removeDuplicates(s = "deeedbbcccbdaa", k = 3)
# %%
# ans = "ps"
s.removeDuplicates(s = "pbbcggttciiippooaais", k = 2)
# %% wa17
s.removeDuplicates(s = "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", k = 4)
# %%
