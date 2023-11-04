class Solution:
    def isValid(self, s: str) -> bool:
        
        # This is the compliments dictionary
        brackets = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        
        # Stack to track the opening and closing of parentheses. We will use LIFO.
        stack = []

        # If uneven length, impossible to be valid.
        if (len(s) % 2) > 0:
            return False
        
        for i in s:
            if i in brackets: # This will only result True if "i" matches a key, which are opening brackets.
                stack.append(i) # add the OPENING parenthesis. 
            if i not in brackets: # If its not in brackets, it could be invalid, or a closing bracket.
                if len(stack) == 0: # If stack is currently empty, then means no opening bracket was previously encountered.
                    return False # -> invalid parentheses
                popped = stack.pop() # get the last added opening bracket.
                if brackets[popped] != i: # Use the brackets dictionary to check if "i" is proper closing bracket.
                    return False

        if len(stack) == 0: # length of our tracking stack should be zero at the end.
            return True # -> VALID parentheses
        else:
            return False
        
testSolution = Solution()
print(testSolution.isValid("[()]")) # Outputs: True
print(testSolution.isValid("[(])")) # Outputs: False

                