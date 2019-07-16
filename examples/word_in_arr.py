class Solution:
    def exist(self, board, word: str) -> bool:
        # start location is first letter
        # check neighbors for next letter
        # if exists, go to that location and check for next letter
        def get_words(i, j, pos=0):
            nonlocal visited
            if pos == len(word):
                return True

            if (
                i < 0
                or i == len(board)
                or j < 0
                or j == len(board[0])
                or visited.get((i, j))
                or word[pos] != board[i][j]
            ):
                return False

            visited[(i, j)] = True
            res = (
                get_words(i, j + 1, pos + 1)
                or get_words(i, j - 1, pos + 1)
                or get_words(i + 1, j, pos + 1)
                or get_words(i - 1, j, pos + 1)
            )
            visited[(i, j)] = False

            return res

        visited = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if get_words(i, j):
                    return True
        return False
