class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_t, t_s = {},{}
        
        for char1, char2 in zip(s,t):
            if(char1 in s_t and s_t[char1] != char2)or(
                char2 in t_s and t_s[char2] != char1):
                return False 
            s_t[char1] = char2
            t_s[char2] = char1
        return True
                
            
        
        
        