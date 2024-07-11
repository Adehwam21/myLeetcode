class Solution:
    def isValid(self, s: str) -> bool:
        valid_pair = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for char in s:
            if char in valid_pair.values():
                stack.append(char)
            elif char in valid_pair.keys():
                if stack and stack[-1] == valid_pair[char]:
                    stack.pop()
                else:
                    return False
        
        return not stack 
    
    '''
    If stack is empty (not stack), it means all open parentheses were matched correctly, because 
    correct matches were poped.
    Otherwise, there is still an invalid sequence so the string won't valid.
    '''

