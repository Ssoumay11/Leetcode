class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # --------------------------------------------------
        # Step 1: Count how many times each character
        # appears in t
        # --------------------------------------------------
        count = {}

        for ch in t:
            count[ch] = count.get(ch, 0) + 1

        # Example:
        # t = "ABC"
        # count = {'A': 1, 'B': 1, 'C': 1}

        i = 0
        j = 0

        # Number of characters from t that we still need
        required = len(t)

        # Store starting position of minimum window
        start = 0

        # Store length of minimum window
        minLength = float('inf')


        # --------------------------------------------------
        # Step 2: Start sliding window
        # j = right side of window
        # i = left side of window
        # --------------------------------------------------
        while j < len(s):

            # Add s[j] into our current window
            if s[j] in count:

                # If we still need this character,
                # then we have now found one required character
                if count[s[j]] > 0:
                    required -= 1

                # Decrease the required count
                count[s[j]] -= 1


            # --------------------------------------------------
            # Step 3: If required == 0,
            # current window contains all characters of t
            # --------------------------------------------------
            while required == 0:

                # Check if current window is smaller
                # than our previous answer
                if j - i + 1 < minLength:

                    minLength = j - i + 1
                    start = i


                # --------------------------------------------------
                # Step 4: Remove the left character
                # to make the window smaller
                # --------------------------------------------------
                if s[i] in count:

                    count[s[i]] += 1

                    # If count becomes positive,
                    # it means we removed a required character
                    if count[s[i]] > 0:
                        required += 1

                # Move left pointer forward
                i += 1


            # Move right pointer forward
            j += 1


        # --------------------------------------------------
        # Step 5: If no valid window was found
        # --------------------------------------------------
        if minLength == float('inf'):
            return ""

        # Return the minimum window
        return s[start:start + minLength]