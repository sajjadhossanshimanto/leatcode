'''
https://leetcode.com/problems/simplify-path/description/
'''
#%%
from typing import List
from itertools import chain


inf = float('inf')
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        no_action = (".", "/", "")
        ans = []
        for i in path:
            if i =="..":
                # security for pop
                if ans: ans.pop()
            elif i not in no_action:
                ans.append(i)# normal folder name
                
        return "/"+"/".join(ans)

s = Solution()
# %%
p=r"top sort//..//top sort//readme.md"
#%%
p="/home/"
p= "/home//foo/"
p="/home/user/Documents/../Pictures"
p= "/../"
p="/.../a/../b/c/../d/./"
s.simplifyPath(p)
# %% wa190
p="/../"
s.simplifyPath(p)

# %%
