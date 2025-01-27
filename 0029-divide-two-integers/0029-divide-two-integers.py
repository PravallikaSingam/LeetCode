class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle the edge case for overflow
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive values for simplicity
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Perform the division using subtraction
        quotient = 0
        while dividend >= divisor:
            # Optimize subtraction using bit shifting
            temp_divisor, num_divisors = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                num_divisors <<= 1
            
            # Subtract the largest shifted divisor and add the count
            dividend -= temp_divisor
            quotient += num_divisors
        
        # Apply the sign
        if negative:
            quotient = -quotient
        
        # Clamp the result to the 32-bit signed integer range
        return max(INT_MIN, min(INT_MAX, quotient))

        