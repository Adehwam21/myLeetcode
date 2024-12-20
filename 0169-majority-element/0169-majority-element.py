class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        majority = 0
        threshold = len(nums) / 2

        for i in range(0, len(nums)):
            if nums[i] in counts:
                counts[nums[i]] += 1
            else:
                counts[nums[i]] = 1

        val = list(counts.values())
        elements = list(counts.keys())

        max_count = max(val)
        if max_count > threshold:
            majority = val.index(max_count)
        return elements[majority]
        