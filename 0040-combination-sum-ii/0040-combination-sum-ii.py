class Solution:
    def combinationSum2(self, candidates, target):

        result = []

        candidates.sort()

        def backtrack(start, target, temp):

            # Target achieved
            if target == 0:
                result.append(temp.copy())
                return

            # Target exceeded
            if target < 0:
                return

            for i in range(start, len(candidates)):

                # Skip duplicate choices
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Since array is sorted
                if candidates[i] > target:
                    break

                # Take
                temp.append(candidates[i])

                # i + 1 because each element can be used only once
                backtrack(i + 1, target - candidates[i], temp)

                # Backtrack
                temp.pop()

        backtrack(0, target, [])

        return result