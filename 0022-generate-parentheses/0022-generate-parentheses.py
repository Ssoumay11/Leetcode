class Solution:
    def solve(self, n, open_count, close_count, temp, result):

        # Base Case
        if len(temp) == 2 * n:
            result.append(temp)
            return

        # Add opening bracket
        if open_count < n:
            self.solve(n, open_count + 1, close_count, temp + "(", result)
        # Add closing bracket
        if close_count < open_count:
                  self.solve(n, open_count, close_count + 1, temp + ")", result)

    def generateParenthesis(self, n: int):

        result = []

        # Start recursion
        self.solve(n, 0, 0, "", result)

        return result


        
