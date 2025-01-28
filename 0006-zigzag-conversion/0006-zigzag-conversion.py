class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: if numRows is 1, the zigzag pattern is the same as the input string
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create an array to hold the strings for each row
        rows = [''] * numRows
        current_row = 0  # Start at the first row
        going_down = False  # Direction control
        
        # Iterate over each character in the string
        for char in s:
            rows[current_row] += char  # Append the character to the current row
            
            # If we're at the top or bottom row, change direction
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            # Move to the next row (up or down based on direction)
            current_row += 1 if going_down else -1
        
        # Combine all rows to form the final zigzag string
        return ''.join(rows)

        