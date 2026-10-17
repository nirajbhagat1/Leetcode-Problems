
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    bit = 1 << (int(board[i][j]) - 1)
                    rows[i] |= bit
                    cols[j] |= bit
                    boxes[(i // 3) * 3 + j // 3] |= bit

        def solve(pos):
            if pos == len(empty):
                return True

            # Choose the empty cell with the fewest candidates (MRV)
            best = pos
            best_mask = 0
            min_count = 10

            for k in range(pos, len(empty)):
                i, j = empty[k]
                b = (i // 3) * 3 + j // 3
                mask = 0x1FF & ~(rows[i] | cols[j] | boxes[b])
                count = mask.bit_count()

                if count < min_count:
                    min_count = count
                    best = k
                    best_mask = mask

                if count == 0:
                    return False
                if count == 1:
                    break

            empty[pos], empty[best] = empty[best], empty[pos]
            i, j = empty[pos]
            b = (i // 3) * 3 + j // 3

            mask = 0x1FF & ~(rows[i] | cols[j] | boxes[b])

            while mask:
                bit = mask & -mask
                mask ^= bit
                digit = bit.bit_length()

                board[i][j] = str(digit)
                rows[i] |= bit
                cols[j] |= bit
                boxes[b] |= bit

                if solve(pos + 1):
                    return True

                rows[i] ^= bit
                cols[j] ^= bit
                boxes[b] ^= bit
                board[i][j] = "."

            empty[pos], empty[best] = empty[best], empty[pos]
            return False

        solve(0)
