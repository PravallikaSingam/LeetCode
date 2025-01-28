class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1  # Any number raised to the power of 0 is 1
        
        if n < 0:
            x = 1 / x  # Convert negative power to reciprocal
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:  # If n is odd, multiply the result by x
                result *= x
            x *= x  # Square the base
            n //= 2  # Divide n by 2 (integer division)

        return result

        