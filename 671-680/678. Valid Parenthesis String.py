class Solution:
    def checkValidString(self, s: str) -> bool:
        asteCount = 0
        leftCount = 0
        stack = []

        for c in s:
            if c == '*':
                asteCount+=1
            elif c == '(':
                leftCount+=1
            elif c == ')':
                if leftCount == 0:
                    return False
                elif 