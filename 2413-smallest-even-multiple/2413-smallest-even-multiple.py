class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        multiples = [n * i for i in range(1, 3)]
        
        if n % 2 != 0:
            return max(multiples)
        else:
            return min(multiples)
            