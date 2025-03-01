# https://leetcode.com/problems/powx-n/
'''
leetcode medium. because 
the power can be negative as well

'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = x
        for _ in range(abs(n)-1):
            ans*=x
        
        return 1/ans if n<0 else ans