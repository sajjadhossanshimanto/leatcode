'''
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
'''
#%%
class Solution:
    def removeDuplicates(self, s: str) -> int:
        counter = []# (char, count)# like Counter dataclass
        for char in s:
            if counter and counter[-1][0]==char:
                counter[-1][1] += 1
            else:
                counter.append([char, 1])

            if counter[-1][1]>1:
                counter.pop()

        return "".join(i for i, _ in counter)

s = Solution()
#%%
class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Create a stack to store characters.
        st = []

        # Iterate through each character of the input string.
        for char in s:
            # Check if the stack is not empty.
            if st:
                # If the current character is equal to the top of the stack, remove the duplicate.
                if st[-1] == char:
                    st.pop()
                else:
                    # Push the current character onto the stack.
                    st.append(char)
            else:
                # If the stack is empty, push the current character onto the stack.
                st.append(char)

        # Build the result string by joining characters from the stack.
        result = ''.join(st)

        return result

s = Solution()
s.removeDuplicates(s = "aeeed")
# %%
# ans = "abcd"
s.removeDuplicates(s = "abcd")
# %%
# %%
# ans = "ca"
s.removeDuplicates(s = "abbaca")
# %% 
ans = "ay"
s.removeDuplicates(s = "azxxzy")
# %%
