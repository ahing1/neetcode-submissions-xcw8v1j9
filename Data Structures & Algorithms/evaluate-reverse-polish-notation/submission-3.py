class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in operators:
                num2 = stack.pop()
                num1 = stack.pop()

                if tokens[i] == '+':
                    res = num1 + num2
                    stack.append(res)
                elif tokens[i] == '-':
                    res = num1 - num2
                    stack.append(res)
                elif tokens[i] == '*':
                    res = num1 * num2
                    stack.append(res)
                elif tokens[i] == '/':
                    res = int(num1 / num2)
                    stack.append(res)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]