class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        reverse = ""
        right = len(s)-1
        left = 0
        
        while left < right:
            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            left += 1
            right -= 1
        
        i = 0
        while i <= len(s)-2:
            reverse = reverse + s[i] + " " 
            i += 1
        reverse = reverse + s[len(s)-1]
        return reverse
        
            
            