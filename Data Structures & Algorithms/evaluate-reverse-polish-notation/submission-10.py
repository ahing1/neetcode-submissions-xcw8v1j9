class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        operands = {"+", "-", "*", "/"}

        for i in range(len(tokens)):
            if tokens[i] in operands:
                num2 = stack.pop()
                num1 = stack.pop()

                if tokens[i] == "+":
                    stack.append(num1 + num2)
                elif tokens[i] == "-":
                    stack.append(num1 - num2)
                elif tokens[i] == "*":
                    stack.append(num1 * num2)
                elif tokens[i] == "/":
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]
