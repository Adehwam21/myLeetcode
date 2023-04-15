class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #   because the list is sorted in ascending order, two pointers are used
        left = 0
        right = len(nums)-1
        
        while left <= right:
            middle = (left + right) // 2    # middle item of the items between the pointers
            
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1