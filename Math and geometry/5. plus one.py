# https://leetcode.com/problems/plus-one/description/

#%%7
from typing import List


def single_plus(a, b):
    return divmod(a+b, 10)

#%%
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cur = len(digits)-1
        carry = 1
        while cur>=0:
            carry, _sum = single_plus(digits[cur], carry)
            digits[cur] = _sum
            if not carry:
                return digits

            cur-=1

        if carry:
            digits.insert(0, carry)
        
        return digits

s=Solution()
#%%
plus_one(5)
# %%
s.plusOne([4,3,2,1])
# %%
