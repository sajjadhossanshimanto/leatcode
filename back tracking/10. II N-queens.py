'''
https://leetcode.com/problems/n-queens-ii/description/
'''
#%%
from typing import List


class Solution:
    def totalNQueens(self, n: int) -> int:
        visit_col = set()
        left_corner = set()# if used arr need n+n space
        right_corner = set()

        count = [0]
        def dfs_row(x):
            for y in range(n):
                if y in visit_col or (x+y) in left_corner or (x-y) in right_corner : continue

                # place_queen(x, y)
                visit_col.add(y)
                right_corner.add(x-y)
                left_corner.add(x+y)

                if x<n-1:# next row exists
                    dfs_row(x+1)
                if x==n-1:
                    count[0]+=1

                # remove queen
                visit_col.remove(y)
                right_corner.remove(x-y)
                left_corner.remove(x+y)

        dfs_row(0)
        return count[0]


s = Solution()
# %%
s.totalNQueens (4)
# %%
s.totalNQueens(1)
# %%
