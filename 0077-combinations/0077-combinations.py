class Solution:

    def __init__(self):
        self.result = []

    def solve(self, start, n, k, temp):

        # Base case
        if k == 0:
            self.result.append(temp.copy())
            return

        if start > n:
            return

        # Take
        temp.append(start)
        self.solve(start + 1, n, k - 1, temp)

        # Backtrack
        temp.pop()

        # Don't take
        self.solve(start + 1, n, k, temp)

    def combine(self, n: int, k: int) -> list[list[int]]:

        temp = []

        self.solve(1, n, k, temp)

        return self.result