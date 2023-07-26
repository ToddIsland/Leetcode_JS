class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        length, width = len(board[0]), len(board)

        string = ""

        def iter(i, j):
            nonlocal string
            if i == width:
                return
            if j == length:
                return

            string += board[i][j]
            if string == word:
                return True

            iter(i + 1, j)
            string = string[:-1]
            iter(i, j + 1)

        iter(0, 0)

        return False
