# https://leetcode.com/problems/multiply-strings/
'''
num1 and num2 -> are digits only
    - so no sign and so no negative value

'''
# TODO: in case int convertion is not usable at all
multi_table = {
    ("1", "1"): "1"
}

#%%
def single_digit(a:str, b:str, carry=0):
    # TODO: am i allowed to at least convert single digit to integer

    return divmod(int(a)*int(b)+carry, 10)

def num_x_digit(num:str, n:str, carry=0):
    ans = 0
    # carry = 0
    place_value = 1
    for i in range(len(num)-1, -1, -1):
        i = num[i]
        carry, _sum = single_digit(i, n, carry)
        ans += _sum*place_value
        place_value*=10
    
    if carry:# NOTE: don't forget to handle carry
        ans+=carry*place_value
    
    return ans


#%%
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # lets think number 1 as upper and number 2 as lower
        # we wil loop through the lower number

        if len(num1)<len(num2):
            num1, num2 = num2,  num1

        ans = 0
        place_value = 1
        for cur in range(len(num2)-1, -1, -1):
            ans += num_x_digit(num1, num2[cur]) * place_value
            
            place_value*=10
        
        return str(ans)

        # 1234
        #   45
        # -----
        #     0

s = Solution()
# %%
s.multiply("9", "9")
# %%
