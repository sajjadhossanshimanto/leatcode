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
        n = len(board)+1# squire board and 1 indexed
        cell = n*n

        maps = {}
        num=1
        for x in range(gx):
            for y in range(gy):
                if board[x][y]!=-1:
                    maps[num] = board[x][y]
                    num+=1
        # num = 1
        visit = [0]*(cell+1)
        adj = [[] for _ in range(cell+1)]
        for i in range(1, cell+1):
            for j in range(i+1, i+7):
                if not visit[j]:
                    visit[j] = 1
                    if j in maps:
                        adj[i].append(maps[j])
                    else:
                        adj[i].append(j)

        # bfs
        q = deque()
        q.append((1, 0))# pos, moves used to reach that node
        while q:
            pos, move = q.popleft()

            for child in adj[pos]:
                # child can't be in visit as it is a directed graph
                if child==cell:
                    return move+1
                q.append(child, move+1)
        return -1

#%%
