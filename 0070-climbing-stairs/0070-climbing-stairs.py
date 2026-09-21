class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1  # Base cases

        prev = 1
        curr = 1  # f(0) = 1, f(1) = 1

        for i in range(2, n + 1):
            temp = curr
            curr = curr + prev  # f(i) = f(i-1) + f(i-2)
            prev = temp

        return curr