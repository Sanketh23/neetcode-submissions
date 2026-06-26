class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            if tokens[i] in operators:
                if tokens[i] == '+':
                    stack.append(stack.pop() + stack.pop())
                elif tokens[i] == '-':
                    temp = stack.pop()
                    stack.append(stack.pop() - temp)
                elif tokens[i] == '*':
                    stack.append(stack.pop() * stack.pop())
                else:
                    temp = stack.pop()
                    stack.append(stack.pop() // temp)
                    print(stack)
            else:
                stack.append(int(tokens[i]))
        return stack[0]