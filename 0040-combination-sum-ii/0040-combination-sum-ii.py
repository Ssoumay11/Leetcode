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

        # Move to next index because
        # each element can be used only once
        self.solve(
            candidates,
            idx + 1,
            target - candidates[idx],
            temp
        )

        # Backtrack
        temp.pop()

        # Skip duplicate elements
        next_idx = idx + 1

        while (
            next_idx < len(candidates)
            and candidates[next_idx] == candidates[idx]
        ):
            next_idx += 1

        # Don't take current element
        self.solve(
            candidates,
            next_idx,
            target,
            temp
        )

    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:

        candidates.sort()

        self.solve(candidates, 0, target, [])

        return self.result