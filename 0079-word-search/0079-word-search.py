class Solution:

    def __init__(self):
        self.m = 0
        self.n = 0
        self.l = 0

        self.directions = [
            (0, 1),   # right
            (0, -1),  # left
            (1, 0),   # down
            (-1, 0)   # up
        ]

    def find(self, board, i, j, word, idx):

        # Base case
        if idx >= self.l:
            return True

        # Out of bounds or character doesn't match
        if (i < 0 or i >= self.m or
            j < 0 or j >= self.n or
            board[i][j] != word[idx]):
            return False

        # Mark current cell as visited
        temp = board[i][j]
        board[i][j] = '#'

        # Explore all 4 directions
        for di, dj in self.directions:

            i_ = i + di
            j_ = j + dj

            if self.find(board, i_, j_, word, idx + 1):
                return True

        # Backtrack
        board[i][j] = temp

        return False

    def exist(self, board, word):

        self.m = len(board)
        self.n = len(board[0])
        self.l = len(word)

        # Not enough cells
        if self.m * self.n < self.l:
            return False

        # Try every cell as starting point
        for i in range(self.m):
            for j in range(self.n):

                if board[i][j] == word[0]:

                    if self.find(board, i, j, word, 0):
                        return True

        return False