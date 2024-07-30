'''
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
'''
#%%
class Solution:
    def removeDuplicates(self, s: str, k: int) -> int:
        counter = []
        string = []
        for char in s:
            c = 1
            if string and string[-1]==char:
                c = counter[-1]+1
            counter.append(c)
            string.append(char)

            if c==k:
                for _ in range(k):
                    counter.pop()
                    string.pop()

        return "".join(string)

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
