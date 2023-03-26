class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a = sum(nums[:i]) # left sum
            b = sum(nums[i+1:]) # right sum
            if (a == b):
                return i
        return -1
