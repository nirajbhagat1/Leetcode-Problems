
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:

        def isSafe(i, j, dig):
            for k in range(9):
                if board[i][k] == dig or board[k][j] == dig:
                    return False

            r, c = (i // 3) * 3, (j // 3) * 3

            for x in range(r, r + 3):
                for y in range(c, c + 3):
                    if board[x][y] == dig:
                        return False

            return True

        def solve():
            best_i = best_j = -1
            best_candidates = None

            # Choose the empty cell with the fewest candidates
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        candidates = []

                        for dig in "123456789":
                            if isSafe(i, j, dig):
                                candidates.append(dig)

                        if not candidates:
                            return False

                        if best_candidates is None or len(candidates) < len(best_candidates):
                            best_i, best_j = i, j
                            best_candidates = candidates

                            if len(candidates) == 1:
                                break

                if best_candidates is not None and len(best_candidates) == 1:
                    break

            if best_candidates is None:
                return True

            for dig in best_candidates:
                board[best_i][best_j] = dig

                if solve():
                    return True

                board[best_i][best_j] = "."

            return False

        solve()
