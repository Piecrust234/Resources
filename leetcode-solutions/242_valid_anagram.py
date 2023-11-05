class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # Setup dictionary/hash map 
        char_count = {} # for each character, set a key (the character) and how many times its been seen.

        # Count the number of times a character has been seen with the map
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Iterate through the other string.
        for char in t:
            if char in char_count and char_count[char] > 0: # If a character from t is in the dictionary, and the count is > 0
                char_count[char] -= 1 # subtract and keep going
            else: # If the character hadn't been seen in the other list, or if the charcount for that character is 0, then they cant be anagrams.
                return False
                
        # Is true because it never returned false        
        return True
        