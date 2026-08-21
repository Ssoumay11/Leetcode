class Solution:

    def solve(self, candidates, target, idx, temp, current_sum, result):

        # Base Case
        if idx == len(candidates):
            if current_sum == target:
                result.append(temp.copy())
            return

        # TAKE
        if current_sum + candidates[idx] <= target:
            temp.append(candidates[idx])
            self.solve(candidates, target, idx, temp, current_sum + candidates[idx], result)
            temp.pop()

        # NOT TAKE
        self.solve(candidates, target, idx + 1, temp, current_sum, result)


    def combinationSum(self, candidates, target):

        result = []
        temp = []

        self.solve(candidates, target, 0, temp, 0, result)

        return result