class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        total_length = len(s)
        letter_count = 0
        
        for char in s:
            if char == letter:
                letter_count += 1
        
        percentage = int((letter_count/total_length) *  100)
        return percentage