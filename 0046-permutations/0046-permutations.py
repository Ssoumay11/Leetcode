class Solution:

    def __init__(self):
        self.result = []
        self.used = set()
        self.n = 0

    def solve(self, temp, nums):

        # Base case
        if len(temp) == self.n:
            self.result.append(temp.copy())
            return

        # Try every number
        for i in range(self.n):

            # If number is already used, skip
            if nums[i] in self.used:
                continue

            # Choose
            temp.append(nums[i])
            self.used.add(nums[i])

            # Explore
            self.solve(temp, nums)

            # Backtrack
            self.used.remove(nums[i])
            temp.pop()

    def permute(self, nums):

        self.n = len(nums)
        temp = []

        self.solve(temp, nums)

        return self.result