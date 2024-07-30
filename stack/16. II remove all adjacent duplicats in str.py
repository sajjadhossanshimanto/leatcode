'''
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
'''
#%%
class Solution:
    def removeDuplicates(self, s: str, k: int) -> int:
        def slice_s(start, end):
            '''both end points are included'''
            return "".join([s[:start], s[end+1:]])

        counter = [1]
        cur=1
        while cur<=len(s)-1 and len(s)>=k:
            char = s[cur]

            c = 1
            if s[cur-1]==char:
                c = counter[cur-1]+1
            counter.append(c)

            if c==k:
                s = slice_s(cur-k+1, cur)# +1 as both end is included
                cur -= (k-1)
                for _ in range(k): counter.pop()
            else:
                cur+=1
        return s

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
