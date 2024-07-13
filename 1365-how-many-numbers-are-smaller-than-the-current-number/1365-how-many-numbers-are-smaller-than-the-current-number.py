class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_copy = sorted(nums)
        count_dict = {}
        
        for i in range(len(nums_copy)):
            if nums_copy[i] not in count_dict:
                count_dict[nums_copy[i]] = i
        
        result = []
        for num in nums:
            result.append(count_dict[num])
        
        return result
