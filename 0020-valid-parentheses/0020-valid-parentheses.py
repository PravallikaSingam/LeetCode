class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to store opening brackets
        stack = []
        
        # Mapping of closing brackets to corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # Iterate over the string
        for char in s:
            if char in bracket_map:
                # Check if the stack is empty or the top of the stack doesn't match
                top_element = stack.pop() if stack else '#'
                if top_element != bracket_map[char]:
                    return False
            else:
                # If the character is an opening bracket, push it to the stack
                stack.append(char)
        
        # If the stack is empty, all brackets matched correctly, otherwise return False
        return not stack

        