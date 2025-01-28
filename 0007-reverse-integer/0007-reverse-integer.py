class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1  # Define 32-bit integer range
        
        res = 0
        sign = 1 if x > 0 else -1  # Determine the sign of the number
        x = abs(x)  # Work with the absolute value of x
        
        while x != 0:
            digit = x % 10  # Extract the last digit
            x //= 10  # Remove the last digit
            
            # Check for overflow/underflow before appending the digit
            if res > (INT_MAX - digit) // 10:
                return 0  # Return 0 if the result goes out of bounds
            
            res = res * 10 + digit  # Append the digit to the reversed number
        
        return res * sign  # Restore the sign

        