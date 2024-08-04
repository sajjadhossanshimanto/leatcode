'''
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
'''
#%%
from typing import List
from itertools import combinations


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = tuple(map(set, arr))
        n = len(arr)

        ans = 0
        for i in range(1, n+1):
            for comb in combinations(arr, r=i):
                # here `comb` is a list of set from power set
                set1 = set()
                for set2 in comb:
                    temp = set1.union(set2)
                    if len(set1) + len(set2) == len(temp):
                        set1 = temp
                    else:
                        break
                else:
                    # if non-breaking
                    ans = max(ans, len(set1))

        return ans

s = Solution()
# %%
# ans = 4
s.maxLength(["un", "iq", "ue"])
# %%
# ans = 6
s.maxLength(arr = ["cha","r","act","ers"])
# %%
# 26
s.maxLength(arr = ["abcdefghijklmnopqrstuvwxyz"])
# %%
