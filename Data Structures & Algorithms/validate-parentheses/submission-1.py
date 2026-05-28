class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenList = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in parenList:
                if stack and stack[-1] == parenList[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False