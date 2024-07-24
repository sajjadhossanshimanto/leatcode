#%%
from typing import List
from itertools import combinations


class Solution:
    def totalNQueens(self, n: int) -> int:
        visit_col = set()
        left_corner = set()# if used arr need n+n space
        right_corner = set()

        def place_queen(x, y):
            # mark col
            visit_col.add(y)

            # mark right-corner
            right_corner.add(x-y)

            # mark left-corner
            left_corner.add(x+y)

        def remove_queen(x, y):
            # mark col
            visit_col.remove(y)

            # mark right-corner
            right_corner.remove(x-y)

            # mark left-corner
            left_corner.remove(x+y)

        count = [0]
        def dfs_row(x):
            available = []
            for y in range(n):
                if y in visit_col or (x+y) in left_corner or (x-y) in right_corner : continue

                place_queen(x, y)                
                if x<n-1:# next row exists
                    dfs_row(x+1)
                if x==n-1:
                    count[0]+=1

                remove_queen(x, y)

        dfs_row(0)
        return count[0]


s = Solution()
# %%
s.totalNQueens (4)
# %%
