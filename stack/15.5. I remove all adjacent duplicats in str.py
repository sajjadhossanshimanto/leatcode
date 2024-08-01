'''
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
'''
#%%
class Solution:
    def removeDuplicates(self, s: str) -> int:
        counter = []# (char, count)# like Counter dataclass
        for char in s:
            if counter and counter[-1][0]==char:
                counter[-1][1] += 1
            else:
                counter.append([char, 1])

            if counter[-1][1]>=2:
                counter.pop()

        return "".join(i for i, _ in counter)

s = Solution()
# %%
# ans = "abcd"
s.removeDuplicates(s = "abcd")
# %%
# ans = ""
s.removeDuplicates(s = "deeedbbcccbdaa")
# %%
# ans = "ca"
s.removeDuplicates(s = "abbaca")
# %% 
ans = "ay"
s.removeDuplicates(s = "azxxzy")
# %%
