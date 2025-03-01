# https://leetcode.com/problems/powx-n/
'''
leetcode medium. because 
the power can be negative as well

notes:
- power would not be negative

edge case:
- power 0 -> is 1
- TODO: what would be for 0^0??
    - we follow zero to the power anything -> 0
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0: return 1# edge case
        if x==0: return 0

        ans = x
        for _ in range(abs(n)-1):
            ans*=x
        
        return 1/ans if n<0 else ans

s = Solution()
'''
gets tle -> as this is of O(N).
we can improve this to O(nlogn).
'''
s.myPow(0.00001, 2147483647)
#%%

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def helper(x, n):
            ''' n has to be posative'''
            if n==0: return 1# edge case
            if x==0: return 0

            ans = helper(x, n//2)
            ans *= ans
            if n&1: ans *=x

            return ans
        
        ans = helper(x, abs(n))
        return 1/ans if n<0 else ans

s = Solution()