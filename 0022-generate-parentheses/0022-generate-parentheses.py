class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(current_str, open_count, close_count):
            # If the current string is of length 2 * n, it's a valid combination
            if len(current_str) == 2 * n:
                result.append(current_str)
                return
            
            # We can add an opening parenthesis if we haven't used all 'n' open parentheses
            if open_count < n:
                backtrack(current_str + "(", open_count + 1, close_count)
            
            # We can add a closing parenthesis if we have more open parentheses than closing ones
            if close_count < open_count:
                backtrack(current_str + ")", open_count, close_count + 1)
        
        # Start the backtracking with an empty string, 0 open and 0 close parentheses
        backtrack("", 0, 0)
        return result


        