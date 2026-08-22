class Solution:

    def __init__(self):
        self.result = []

    def solve(self, candidates, idx, target, temp):

        # Base case
        if target == 0:
            self.result.append(temp.copy())
            return

        # Invalid case
        if idx >= len(candidates) or target < 0:
            return

        # Take
        temp.append(candidates[idx])
        self.solve(
            candidates,
            idx + 1,
            target - candidates[idx],
            temp
        )

        # Backtrack
        temp.pop()

        # Skip duplicate elements
        while (
            idx + 1 < len(candidates)
            and candidates[idx] == candidates[idx + 1]
        ):
            idx += 1

        # Don't take
        self.solve(
            candidates,
            idx + 1,
            target,
            temp
        )

    def combinationSum2(
        self,
        candidates: list[int],
        target: int
    ) -> list[list[int]]:

        candidates.sort()

        temp = []

        self.solve(candidates, 0, target, temp)

        return self.result