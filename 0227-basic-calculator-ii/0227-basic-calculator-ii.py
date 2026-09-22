class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'

        for i, ch in enumerate(s):
            
            # Build the number
            if ch.isdigit():
                num = num * 10 + int(ch)

            # If operator or last character
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:

                if sign == '+':
                    stack.append(num)

                elif sign == '-':
                    stack.append(-num)

                elif sign == '*':
                    stack.append(stack.pop() * num)

                elif sign == '/':
                    prev = stack.pop()
                    stack.append(int(prev / num))

                sign = ch
                num = 0

        return sum(stack)