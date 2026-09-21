class Solution:
    def isValid(self, s):
        stack = []

        for ch in s:

            if ch == '(' or ch == '[' or ch == '{':
                stack.append(ch)

            else:
                if not stack:       # check empty 
                    return False

                top = stack.pop()

                if ch == ')' and top != '(':    #valid tabhi hoga jb “(” present hoga 
                    return False

                if ch == ']' and top != '[':
                    return False

                if ch == '}' and top != '{':
                    return False

        return len(stack) == 0