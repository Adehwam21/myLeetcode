class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)-1
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        for i in range(n - k + 1):
            current_sum = current_sum - nums[i] + nums[i + k]
            max_sum = max(max_sum, current_sum)
        
        return max_sum / k
        