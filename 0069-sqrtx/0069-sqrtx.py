class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x  # 0 -> 0, 1 -> 1

        left, right = 1, x
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                ans = mid  # Store potential answer
                left = mid + 1
            else:
                right = mid - 1
        
        return ans  # Return the floored square root



        