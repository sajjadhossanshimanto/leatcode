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
        l = 0
        for r in range(10, len(s)):
            sub = s[l:r]
            if sub in visit:
                ans.append(sub)
                # ans.append(sub[::-1])
            else:
                visit.add(sub)
                visit.add(sub[::-1])
            l+=1
        
        return ans

s = Solution()
# %%
# ["AAAAACCCCC","CCCCCAAAAA"]
s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
# %%
