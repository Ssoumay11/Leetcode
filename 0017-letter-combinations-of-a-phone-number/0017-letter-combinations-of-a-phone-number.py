class Solution:

    def __init__(self):
        self.result = []

    def solve(self, idx, digits, temp, mp):

        # Base case
        if idx >= len(digits):
            self.result.append("".join(temp))
            return

        ch = digits[idx]
        string = mp[ch]

        for i in range(len(string)):

            # Do
            temp.append(string[i])

            # Recursion
            self.solve(idx + 1, digits, temp, mp)

            # Undo / Backtrack
            temp.pop()

    def letterCombinations(self, digits: str) -> list[str]:

        if len(digits) == 0:
            return []

        mp = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        temp = []

        self.solve(0, digits, temp, mp)

        return self.result