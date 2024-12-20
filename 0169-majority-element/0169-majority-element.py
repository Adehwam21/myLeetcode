class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        threshold = len(nums) / 2

        for i in range(0, len(nums)):
            if nums[i] in count_dict:
                count_dict[nums[i]] += 1
                if count_dict[nums[i]] > threshold:
                    return nums[i]
            else:
                count_dict[nums[i]] = 1
                if count_dict[nums[i]] > threshold:
                    return nums[i]