class Solution:
    def romanToInt(self, s: str) -> int:
        
        map = {
             "I" : 1,
             "V" : 5,
             "X" : 10,
             "L" : 50,
             "C" : 100,
             "D" : 500,
             "M" : 1000}
        
        total = 0
        all_roman = map[s[len(s)-1]]
        
        for i in range(len(s)-1):
            current_roman = map[s[i]]
            next_roman = map[s[i+1]]
            
            if next_roman > current_roman: 
                total -= current_roman
            else:
                total += current_roman

        total += all_roman
        return(total)