# https://leetcode.com/problems/powx-n/
'''
leetcode medium. because 
the power can be negative as well

edge case:
- power 0 -> is 1
- TODO: what would be for 0^0??
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0: return 1# edge case

        ans = x
        for _ in range(abs(n)-1):
            ans*=x
        
        return 1/ans if n<0 else ans

s = Solution()
'''
gets tle -> as we are not considering fractional power
'''
s.myPow(0.00001, 2147483647)
