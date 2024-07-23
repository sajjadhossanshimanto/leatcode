#%%
from typing import List
from itertools import combinations


class Solution:
    def solveNQueens(self, n: int) -> list[str]:
        grid = ["."*n]*n
        visit = [[0]*n for _ in range(n)]
        
        def is_valid(x, y):
            pass

        def place_queen(x, y, place=1):
            # mark row
            visit[x] = [place]*n

            # mark col
            for i in range(n):
                visit[i][y] = place

            # mark right-corner
            for i, j in zip(range(x+1, n), range(y+1, n)):
                visit[i][j] = place

            # mark left-corner
            for i, j in zip(range(x-1, -1, -1), range(y-1, -1, -1)):
                if i<0 or j<0: break

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
                place_queen(x, y)
                if x==n-1:
                    return gen_row(y)

                r = dfs_row(x+1)
                if r:
                    grid = gen_row(y)
                    grid.extend(r)
                    
                    return grid
                else:
                    place_queen(x, y, 0)
            
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
