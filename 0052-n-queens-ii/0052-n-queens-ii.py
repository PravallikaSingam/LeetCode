class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row):
            # If all queens are placed, count this as a solution
            if row == n:
                nonlocal count
                count += 1
                return
            
            for col in range(n):
                # Check if the position is valid
                if col in columns or (row + col) in pos_diagonals or (row - col) in neg_diagonals:
                    continue
                
                # Place the queen
                columns.add(col)
                pos_diagonals.add(row + col)
                neg_diagonals.add(row - col)
                
                # Recur to place the next queen
                backtrack(row + 1)
                
                # Backtrack: remove the queen
                columns.remove(col)
                pos_diagonals.remove(row + col)
                neg_diagonals.remove(row - col)
        
        # Initialize sets to track occupied columns and diagonals
        columns = set()
        pos_diagonals = set()  # Tracks positive diagonals (row + col)
        neg_diagonals = set()  # Tracks negative diagonals (row - col)
        
        count = 0  # Number of valid solutions
        backtrack(0)
        return count

        