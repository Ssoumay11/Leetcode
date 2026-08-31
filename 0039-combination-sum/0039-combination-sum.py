class Solution:

    """def __init__(self):
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
        )"""

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:


        result = []

        def backtrack(start, target, temp):

            # Target achieved
            if target == 0:
                result.append(temp.copy())
                return

            # Target exceeded
            if target < 0:
                return

            for i in range(start, len(candidates)):

                # Take
                temp.append(candidates[i])

                # Same i because we can reuse the number
                backtrack(i, target - candidates[i], temp)

                # Backtrack
                temp.pop()

        backtrack(0, target, [])

        return result