'''
https://leetcode.com/problems/surrounded-regions/description/
'''
#%%
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        gx, gy = len(board), len(board[0])

        visit = [[0]*gy for _ in range(gx)]
        def dfs(x, y):
            visit[x][y]=1

            for cx, cy in (
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1)
            ):
                if 0<=cx<gx and 0<=cy<gy and board[cx][cy]=='O' and not visit[cx][cy]:
                    dfs(cx, cy)

        def in_place(x, y):
            board[x][y] = "X"
            
            for cx, cy in (
                (x+1, y),
                (x-1, y),
                (x, y+1),
                (x, y-1)
            ):
                # if 0<=cx<gx and 0<=cy<gy:
                #     (cx, cy) not in visit:
                if board[cx][cy]!='X':
                    in_place(cx, cy)

        for x in range(gx):
            for y in range(gy):
                if board[x][y]=='O' and (x in (0, gx-1) or y in (0, gy-1)):
                    dfs(x, y)

        for x in range(gx):
            for y in range(gy):
                if board[x][y]=='O' and not visit[x][y]:
                    in_place(x, y)

g = Solution()
#%%
inp = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
g.solve(inp)
print(inp)
inp ==  [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# %%
inp = [["X"]]
g.solve(inp)
print(inp)
# %%
