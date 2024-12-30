# https://leetcode.com/problems/unique-paths/description/

#%%
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = [0]
        # visit = [[0 for _ in range(n)] for _ in range(m)]
        def dfs(x, y):
            if x==m-1 and y==n-1:
                count[0]+=1
                return
            # if x>=m or y>=n or x<0 or y<0 or visit[x][y]: return
            if x>=m or y>=n or x<0 or y<0: return

            # visit[x][y] = 1
            dfs(x+1, y)
            dfs(x, y+1)

        dfs(0, 0)
        return count[0]

s = Solution()
# %%
s.uniquePaths(m = 3, n = 7)
# %%
s.uniquePaths(3, 2)
# %% tl
s.uniquePaths(23, 12)

# %%
