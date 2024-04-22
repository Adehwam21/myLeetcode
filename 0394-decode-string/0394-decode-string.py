class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                
                kstr = ""
                while stack and stack[-1].isdigit():
                    kstr = stack.pop() + kstr
                stack.append(int(kstr) * substr)
                
        return "".join(stack)
                