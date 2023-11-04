class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        
        stack = []

        if (len(s) % 2) > 0:
            return False
        
        for i in s:
            if i in brackets:
                stack.append(i)
            if i not in brackets:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if brackets[popped] != i:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
        
testSolution = Solution()
print(testSolution.isValid("[()]")) # Outputs: True
print(testSolution.isValid("[(])")) # Outputs: False

                