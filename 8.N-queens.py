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
            visit[0] = [place]*n

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

        for x in range(n):
            for y in range(n):
                if not visit[x][y]:
                    place_queen(x, y, place=1)
                    break

# %%
