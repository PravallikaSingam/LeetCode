from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        for i in range(n - 1, -1, -1):  # Start from the last digit
            if digits[i] < 9:
                digits[i] += 1  # Simply increment and return
                return digits
            digits[i] = 0  # If digit is 9, set it to 0 and continue
        
        # If all digits were 9, we need an extra 1 at the beginning
        return [1] + digits

# Example test cases
sol = Solution()
print(sol.plusOne([1,2,3]))  # Output: [1,2,4]
print(sol.plusOne([4,3,2,1]))  # Output: [4,3,2,2]
print(sol.plusOne([9]))  # Output: [1,0]
print(sol.plusOne([9,9,9]))  # Output: [1,0,0,0]
