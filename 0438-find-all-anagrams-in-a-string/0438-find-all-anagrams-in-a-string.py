class Solution:
    def allZero(self, count):
        return count == [0] * 26

    def findAnagrams(self, s: str, p: str):
        k = len(p)
        count = [0] * 26

        # Count characters in pattern p
        for ch in p:
            count[ord(ch) - ord('a')] += 1

        i = 0
        j = 0
        n = len(s)
        result = []

        while j < n:
            # Add current character of s
            idx = ord(s[j]) - ord('a')
            count[idx] -= 1

            # Window size == pattern size
            if j - i + 1 == k:

                # If frequencies match
                if self.allZero(count):
                    result.append(i)

                # Remove leftmost character
                count[ord(s[i]) - ord('a')] += 1
                i += 1

            j += 1

        return result