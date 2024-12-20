class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        majority = 0
        threshold = len(nums) / 2

        for i in range(0, len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
                if counts[nums[i]] > threshold:
                    return nums[i]
            else:
                counts[nums[i]] = 1
                if counts[nums[i]] > threshold:
                    return nums[i]
        