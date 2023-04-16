class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_map = {}
    
        # maping charactes with their counts
        for char in s:
            if char not in char_map:
                char_map[char] = 1
            else:
                char_map[char] += 1
                
        total,odd = 0,0
        
        if len(char_map) == 1:
            return char_map[s[0]]
        
        for i in char_map.values():
            if i > 1:
                if i % 2 == 0:
                    total += i
                else:
                    total += i-1
                    odd += 1
            else:
                odd += 1
        if odd > 0:
            total += 1
        return total
        