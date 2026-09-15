class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        n = len(s)

        # If k = 1, every character is a palindrome
        if k == 1:
            return n

        result = 0
        i = 0

        while i <= n - k:

            # Check substring of length k
            if i + k <= n:
                sub = s[i:i + k]

                if sub == sub[::-1]:
                    result += 1
                    i += k
                    continue

            # Check substring of length k + 1
            if i + k + 1 <= n:
                sub = s[i:i + k + 1]

                if sub == sub[::-1]:
                    result += 1
                    i += k + 1
                    continue

            # No palindrome found
            i += 1

        return result