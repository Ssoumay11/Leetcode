class Solution:

    def __init__(self):
        self.result = []

    def solve(self, candidates, idx, target, temp):

        # Target reached
        if target == 0:
            self.result.append(temp.copy())
            return

        # Invalid case
        if target < 0 or idx >= len(candidates):
            return

        # Take current element
        temp.append(candidates[idx])

        # Same element can be used again
        self.solve(
            candidates,
            idx,
            target - candidates[idx],
            temp
        )

        # Backtrack
        temp.pop()

        # Don't take current element
        self.solve(
            candidates,
            idx + 1,
            target,
            temp
        )

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        self.solve(candidates, 0, target, [])

        return self.result