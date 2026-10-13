class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result=[]
        
        def isSafe(i, j):
            # Check upper column
            for k in range(i):
                if board[k][j] == "Q":
                    return False
            # Check upper-left diagonal
            k, l = i - 1, j - 1
            while k >= 0 and l >= 0:
                if board[k][l] == "Q":
                    return False
                k -= 1
                l -= 1
            # Check upper-right diagonal
            k, l = i - 1, j + 1
            while k >= 0 and l < n:
                if board[k][l] == "Q":
                    return False
                k -= 1
                l += 1
            return True
        board = [["." for j in range(n)] for i in range(n)]

        def placeQueens(i):
            # All queens placed
            if i == n:
                result.append(["".join(row) for row in board])
                return

            # Try each column in the current row
            for j in range(n):
                if isSafe(i, j):
                    board[i][j] = "Q"

                    placeQueens(i + 1)

                    # Backtrack
                    board[i][j] = "."

        placeQueens(0)
        return result