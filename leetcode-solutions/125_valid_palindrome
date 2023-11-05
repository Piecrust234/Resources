class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower() # lowercases everything
        
        alphanumstr = "" # initial empty string

        for char in lower: #loop through each char
            if char.isalnum(): #check if the char is alphanumeric
                alphanumstr = alphanumstr + char # if true, append to end of newstring

        reverse = alphanumstr[::-1] # reverse the alphanumeric string

        if alphanumstr == reverse: # check if these are equal
            return True

        return False