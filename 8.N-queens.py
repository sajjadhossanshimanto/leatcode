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

        def dfs_row(x=0):
            available = []
            for y in range(n):
                if y in visit_col or (x+y) in left_corner or (x-y) in right_corner : continue

                place_queen(x, y)# as x is zero based but zero means empty
                # print("placed at ->", x, y)
                # print_grid(visit)
                if x==n-1:# base case
                    return gen_row(y)

                r = dfs_row(x+1)
                if r:
                    grid = gen_row(y)
                    grid.extend(r)
                    
                    return grid
                else:
                    remove_queen(x, y, place=0, inplace=x+1)

            return False

        return dfs_row()


s = Solution()
# %%
s.solveNQueens(4)
# %%
