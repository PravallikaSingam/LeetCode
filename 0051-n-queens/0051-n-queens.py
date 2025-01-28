class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        def backtrack(row):
            if row == n:
                # All queens placed successfully; create a solution
                board = ["".join(row) for row in chessboard]
                solutions.append(board)
                return
            
            for col in range(n):
                # Check if the position is valid
                if col in columns or (row + col) in pos_diagonals or (row - col) in neg_diagonals:
                    continue
                
                # Place the queen
                chessboard[row][col] = "Q"
                columns.add(col)
                pos_diagonals.add(row + col)
                neg_diagonals.add(row - col)
                
                # Recur for the next row
                backtrack(row + 1)
                
                # Backtrack: remove the queen
                chessboard[row][col] = "."
                columns.remove(col)
                pos_diagonals.remove(row + col)
                neg_diagonals.remove(row - col)
        
        solutions = []
        chessboard = [["."] * n for _ in range(n)]
        columns = set()  # Tracks columns with queens
        pos_diagonals = set()  # Tracks positive diagonals (row + col)
        neg_diagonals = set()  # Tracks negative diagonals (row - col)
        
        backtrack(0)
        return solutions
