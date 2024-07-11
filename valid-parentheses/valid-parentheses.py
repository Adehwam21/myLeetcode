class Solution:
    def isValid(self, s: str) -> bool:
        valid_pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        stack = []
        open_par = valid_pair.values()
        close_par = valid_pair.keys()
        
        for char in s:
            if char in open_par:
                stack.append(char)
            elif char in close_par:
                if stack and stack[-1] == valid_pair[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False
        
        return not stack
