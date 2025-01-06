class Solution:
    def isPalindrome(self, s: str) -> bool:
        formated = ""
        for char in s:
            if char.isalpha() or char.isnumeric():
                formated += char.lower()
        
        return formated == formated[::-1]
        