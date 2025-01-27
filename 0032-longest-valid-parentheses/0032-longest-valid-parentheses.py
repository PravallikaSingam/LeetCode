class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        stack = [-1]  # Initialize a stack with -1 to handle the base case

        for i, char in enumerate(s):
            if char == '(':
                # Push the index of '(' onto the stack
                stack.append(i)
            else:
                # Pop the last '(' index
                stack.pop()
                if not stack:
                    # If the stack is empty, push the current index as a base for the next valid substring
                    stack.append(i)
                else:
                    # Calculate the length of the current valid substring
                    max_length = max(max_length, i - stack[-1])
        
        return max_length

        