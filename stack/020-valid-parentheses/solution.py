class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', '}': '{', ']': '['}        
        for c in s:
            if c not in match:
                stack.append(c)
                continue
            if stack and stack[-1] == match[c]:
                stack.pop()
            else:
                return False
        return not stack

