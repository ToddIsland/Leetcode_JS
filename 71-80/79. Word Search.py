class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        path = set()  # position (c, r)

        def iter(c, r, i):
            if i == len(word):
                return True
            if (
                c < 0
                or r < 0
                or c >= COLS
                or r >= ROWS
                or (c, r) in path
                or board[r][c] != word[i]
            ):
                return False

            path.add((c, r))
            res = (
                iter(c - 1, r, i + 1)
                or iter(c + 1, r, i + 1)
                or iter(c, r - 1, i + 1)
                or iter(c, r + 1, i + 1)
            )
            path.remove((c, r))

            return res

        for r in range(ROWS):
            for c in range(COLS):
                if iter(c, r, 0):
                    return True

        return False
