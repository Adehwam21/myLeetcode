class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        final = original
        for num in nums:
            if final not in nums:
                return final
            final = final * 2
        return final

