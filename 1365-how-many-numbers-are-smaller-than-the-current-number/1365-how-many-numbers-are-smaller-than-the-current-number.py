class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        i, j = 0, 0
        result = [0] * len(nums)
        
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    count += 1
            result[i] = count
        
        return result
    