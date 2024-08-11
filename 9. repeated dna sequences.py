'''
https://leetcode.com/problems/repeated-dna-sequences/description/
'''
#%%
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10: return []

        ans = set()
        visit = set()
        for l in range(len(s)-9):
            sub = s[l:l+10]
            if sub in visit:
                ans.add(sub)
            visit.add(sub)

        return ans

s = Solution()
# %%
# ["AAAAACCCCC","CCCCCAAAAA"]
s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
# %%
