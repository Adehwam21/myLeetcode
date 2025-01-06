class Solution:
    def isPalindrome(self, s: str) -> bool:
        formated = ""
        formated = ''.join(char.lower() for char in s if char.isalnum())
        return formated == formated[::-1]
        