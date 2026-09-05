class Solution:

    def __init__(self):
        self.n = 0

    # Reference pass in C++ → Python passes objects by reference
    def isPalindrome(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

    def solve(self, result, temp, s, idx):

        # Base case
        if idx == self.n:
            result.append(temp.copy())
            return

        for i in range(idx, self.n):

            if self.isPalindrome(idx, i, s):

                # Take
                temp.append(s[idx:i + 1])

                # Explore
                self.solve(result, temp, s, i + 1)

                # Backtrack
                temp.pop()

    def partition(self, s):
        self.n = len(s)

        result = []
        temp = []

        self.solve(result, temp, s, 0)

        return result