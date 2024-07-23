#%%
from typing import List
from itertools import combinations


class Solution:
    def solveNQueens(self, n: int) -> list[str]:
        grid = ["."*n]*n
        visit = [[0]*n for _ in range(n)]

        def is_valid(x, y):
            pass

        def place_queen(x, y, inplace=0, place=1):
            # mark row
            for j in range(n):
                if visit[x][j]==inplace:
                    visit[x][j] = place

            # mark col
            for i in range(n):
                if visit[i][y]==inplace:
                    visit[i][y] = place

            # mark right-corner
            for i, j in zip(range(x+1, n), range(y+1, n)):
                if visit[i][j]==inplace:
                    visit[i][j] = place

            # mark left-corner
            for i, j in zip(range(x-1, -1, -1), range(y-1, -1, -1)):
                if i<0 or j<0: break

                if visit[i][j]==inplace:
                    visit[i][j] = place

        def gen_row(y):
            grid = ["."]*n
            grid[y] = "Q"
            return ["".join(grid)]

        def dfs_row(x=0):
            available = []
            for y in range(n):
                if not visit[x][y]:
                    available.append((x, y))

            grid = []
            for x, y in available:
                # print_grid(visit)
                place_queen(x, y, place=x+1)# as x is zero based but zero means empty
                # print("placed at ->", x, y)
                # print_grid(visit)
                if x==n-1:
                    return gen_row(y)

                r = dfs_row(x+1)
                if r:
                    grid = gen_row(y)
                    grid.extend(r)
                    
                    return grid
                else:
                    place_queen(x, y, place=0, inplace=x+1)
            
            return False

        # for x in range(n):
        #     available = []
        #     for y in range(n):
        #         if not visit[x][y]:
        #             available.append((x, y))

        #     for x, y in available:
        #         place_queen(x, y)
        return dfs_row()


s = Solution()
# %%
s.solveNQueens(4)
# %%
