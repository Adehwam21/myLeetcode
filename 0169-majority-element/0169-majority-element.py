class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        cnt = 1
        nums.sort()
        
        for i in range(1, n):
            if nums[i - 1] == nums[i]:
                cnt += 1
            else:
                if cnt > n // 2:
                    return nums[i - 1]
                cnt = 1
        
        # Check the last element
        if cnt > n // 2:
            return nums[-1]