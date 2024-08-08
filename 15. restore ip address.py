'''
https://leetcode.com/problems/restore-ip-addresses/
'''
#%%
from typing import List
from itertools import combinations


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)==4:
            return [".".join(s)]
        
        n = len(s)
        shift = 12 - n
        ips = []
        def backtrack(start, shift, path):
            # valadity checks. checks can be done befor call and after call as well
            # here if i do checks before call i have to repeat same code twice
            # checks apare before basecase so that even the last callback get checked
            if path and len(path[-1])>1 and path[-1][0]=="0":
                # leading zero not valid
                return
            if path and path[-1]=="": return
            if path and int(path[-1]) > 255: return
            
            # base case
            if len(path)==4:
                if not shift:
                    ips.append(".".join(path))
                return 

            # recurtion
            if not shift:
                path.append(s[start:start+3])
                backtrack(start+3, 0, path)
                path.pop()
            else:
                take = 2# max take 0,1,2
                if shift<2:
                    take = shift
                for i in range(take+1):
                    path.append(s[start:start+3-i])
                    backtrack(start+3-i, shift-i, path)
                    path.pop()
        
        backtrack(0, shift, [])
        return ips

s=Solution()
# %%
# ["255.255.11.135","255.255.111.35"]
s.restoreIpAddresses("25525511135")
# %%
# ["0.0.0.0"]
s.restoreIpAddresses("0000")
# %%
# ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
s.restoreIpAddresses("101023")
# %%
