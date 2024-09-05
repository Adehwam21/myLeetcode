class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reverse_x = x[::-1]
        return x == reverse_x
        