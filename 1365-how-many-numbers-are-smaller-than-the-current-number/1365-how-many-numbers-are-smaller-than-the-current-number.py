class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_copy = nums.copy()
        nums_copy.sort()
        
        count_dict = {}
        
        for i in range(len(nums_copy)):
            if nums_copy[i] not in count_dict:
                count_dict[nums_copy[i]] = nums_copy.index(nums_copy[i])
        
        for i in range(len(nums)):
            if nums[i] in count_dict:
                nums[i] = count_dict[nums[i]]
        return nums
                    
