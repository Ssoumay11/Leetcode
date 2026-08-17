class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        maximum_sum = float('-inf')
        for num in nums:
            current_sum += num
            maximum_sum = max(maximum_sum, current_sum)
            if current_sum < 0:
                current_sum = 0
        return maximum_sum