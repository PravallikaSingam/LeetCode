class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1  # Pointers for a and b
        carry = 0
        result = []
        
        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            
            total = bit_a + bit_b + carry
            result.append(str(total % 2))  # Append the binary digit
            carry = total // 2  # Compute the new carry
            
            i -= 1
            j -= 1
        
        return ''.join(result[::-1])  # Reverse the result to get the correct order

# Example test cases
sol = Solution()
print(sol.addBinary("11", "1"))  # Output: "100"
print(sol.addBinary("1010", "1011"))  # Output: "10101"
