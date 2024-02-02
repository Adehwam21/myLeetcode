class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n1 = sys.maxsize
        n2 = sys.maxsize
        n3 = None
        
        for i in range(len(nums)):
            if nums[i] > n2:
                n3 = nums[i]
                return True
            if nums[i] < n1:
                n1 = nums[i]
            elif nums[i] > n1:
                n2 = nums[i]
        return False
            