class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = sum(nums)
        sum_of_N = n*(n+1)/2 # formula for finding sum of natural numbers
        return int(sum_of_N - s)
                