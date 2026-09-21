class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s1)
        m = len(s2)

        # If s1 is larger than s2,
        # no permutation can exist
        if n > m:
            return False

        # Frequency array for s1
        s1_freq = [0] * 26

        # Frequency array for current window of s2
        s2_freq = [0] * 26

        # Count characters of s1
        for i in range(n):
            index = ord(s1[i]) - ord('a')
            s1_freq[index] += 1

        # Sliding window
        i = 0
        j = 0

        while j < m:

            # Add current character to window
            index = ord(s2[j]) - ord('a')
            s2_freq[index] += 1

            # If window becomes bigger than s1,
            # remove the leftmost character
            if j - i + 1 > n:

                index = ord(s2[i]) - ord('a')
                s2_freq[index] -= 1

                i += 1

            # Compare both frequency arrays
            if s1_freq == s2_freq:
                return True

            # Move right pointer
            j += 1

        return False