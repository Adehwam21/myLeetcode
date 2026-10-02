class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = 0, 0
        res_s, res_t = "", ""

        while i < len(s) or j < len(t):
            if i < len(s):
                if s[i] != "#" :
                    res_s += s[i]
                else:
                    res_s = res_s[:-1]
                
                i += 1

            if j < len(t):
                if t[j] != "#":
                    res_t += t[j]
                else:
                    res_t = res_t[:-1]
                
                j += 1
        
        return res_s == res_t