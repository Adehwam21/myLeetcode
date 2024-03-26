class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, mx = 0, 0
        for right, n in enumerate(nums):
            k -= (1 - n)
            if k < 0:
                k+= (1 - nums[left])
                left += 1
            mx = max(mx, (right - left + 1))
        return mx
        