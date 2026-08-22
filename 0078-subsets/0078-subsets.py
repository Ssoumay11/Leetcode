class Solution:
    def __init__(self):
        self.result = []

    def solve(self, nums, idx, temp):

        # Base Case
        if idx >= len(nums):
            self.result.append(temp.copy())
            return

        # TAKE nums[idx]
        temp.append(nums[idx])

        self.solve(nums, idx + 1, temp)
            # BACKTRACK
        temp.pop()

        # NOT TAKE nums[idx]
        self.solve(nums, idx + 1, temp)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = []

        self.solve(nums, 0, temp)

        return self.result

        