class Solution:

    def __init__(self):
        self.result = []

    def solve(self, nums, idx, temp):

        # Base case
        if idx >= len(nums):
            self.result.append(temp.copy())
            return

        # Take
        temp.append(nums[idx])
        self.solve(nums, idx + 1, temp)

        # Backtrack
        temp.pop()

        # Skip duplicate elements
        while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
            idx += 1

        # Don't take
        self.solve(nums, idx + 1, temp)

    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        temp = []

        self.solve(nums, 0, temp)

        return self.result