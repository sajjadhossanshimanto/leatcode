#%%
from typing import List
from itertools import combinations


class Solution:
    def solveNQueens(self, n: int) -> list[str]:
        visit_col = set()
        left_corner = set()# if used arr need n+n space
        right_corner = set()

        def place_queen(x, y):
            # mark col
            visit_col.add(x)

            # mark right-corner
            right_corner.add(x-y)

            # mark left-corner
            left_corner.add(x+y)

        def remove_queen(x, y):
            # mark col
            visit_col.remove(x)

            # mark right-corner
            right_corner.remove(x-y)

            # mark left-corner
            left_corner.remove(x+y)


        def gen_row(y):
            grid = ["."]*n
            grid[y] = "Q"
            return ["".join(grid)]

        grid = []
        def dfs_row(x=0):
            available = []
            for y in range(n):
                if y in visit_col or (x+y) in left_corner or (x-y) in right_corner : continue

                place_queen(x, y)
                grid.append(gen_row(y))
                
                if x<n-1:# next row exists
                    dfs_row(x+1)
                if len(grid)==n:# optimazation: no need to treverse any ferther if sol found
                    return
                remove_queen(x, y)
                grid.pop()

        dfs_row()
        return grid



s = Solution()
# %%
s.solveNQueens(4)
# %%
