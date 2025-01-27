class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Handle edge cases
        if num1 == "0" or num2 == "0":
            return "0"
        
        # Initialize a result array to store the product at each position
        result = [0] * (len(num1) + len(num2))
        
        # Reverse the strings to simplify positional multiplications
        num1 = num1[::-1]
        num2 = num2[::-1]
        
        # Multiply each digit of num1 with each digit of num2
        for i in range(len(num1)):
            for j in range(len(num2)):
                # Multiply digits and add to the current position in result array
                product = int(num1[i]) * int(num2[j])
                result[i + j] += product
                
                # Handle carry
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
        
        # Remove leading zeros from the result array
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        # Convert result array back to a string
        return ''.join(map(str, result[::-1]))

        