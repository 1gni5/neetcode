class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
           '+': lambda a,b : a + b,
           '-': lambda a,b : a - b,
           '*': lambda a,b : a * b,
           '/': lambda a,b : int(a / b),
        }
        stack = []
        for t in tokens:
            if t in op:
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(str(op[t](a, b)))
            else:
                stack.append(t)
        return int(stack[-1])
