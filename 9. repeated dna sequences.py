'''
https://leetcode.com/problems/repeated-dna-sequences/description/
'''
#%%
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10: return []

        ans = []
        visit = set()
        r = len(s)
        l = r-10
        while r>=0:
            sub = s[l:r]
            if sub in visit:
                ans.append(sub)
                l-=10
                r-=10
            else:
                visit.add(sub)
                visit.add(sub[::-1])
                l-=1
                r-=1
        
        return ans

s = Solution()
# %%
# ["AAAAACCCCC","CCCCCAAAAA"]
s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
# %%
