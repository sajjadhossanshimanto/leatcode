'''
https://leetcode.com/problems/snakes-and-ladders/description/
- this question really clears idea witch one and why should a proablem be graph proablem
- jesob question e akta pos thake. abong ak position thake onno position e jete hoy
- hote pare conditional hote pare unconditionally
- egulai graph proablem
'''
#%%
from typing import List
from collections import deque, defaultdict


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # gx, gy = len(board), len(board[0])
        n = len(board)# squire board and 1 indexed
        cell = n*n

        board.reverse()
        def num_to_pos(num):
            x, y = divmod(num-1, n)
            if x&1:
                return x, n-y-1
            return x, y

        # bfs
        visit = set()
        q = deque()
        q.append((1, 0))# pos, moves used to reach that node
        while q:
            pos, move = q.popleft()

            for nxt_pos in range(pos+1, pos+7):
                x, y = num_to_pos(nxt_pos)
                if board[x][y]!=-1:
                    nxt_pos = board[x][y]

                if nxt_pos==cell:
                    return move+1
                
                # avoidend getting visit
                if nxt_pos not in visit:
                    visit.add(nxt_pos)
                    q.append((nxt_pos, move+1))

        return -1

g = Solution()
#%%
# ans = 4
g.snakesAndLadders( [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]])
# %% ml6
g.snakesAndLadders([[1,1,-1],[1,1,1],[-1,1,1]])
# %%
