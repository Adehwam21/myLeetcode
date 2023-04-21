class Solution:
    def climbStairs(self, n: int) -> int:
        # apparently this question can be solved using fibonacci
        
        prev1, prev2 = 1,1

        for i in range(n-1):
            temp = prev1
            prev1 = prev1 + prev2
            prev2 = temp

        return prev1
    