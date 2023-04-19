class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        previous1, previous2 = 1, 0
        result = 0
        for i in range(2, n+1):
            result = previous1 + previous2
            previous2 = previous1
            previous1 = result
            
        return result
            
        
            
            
            
            
        