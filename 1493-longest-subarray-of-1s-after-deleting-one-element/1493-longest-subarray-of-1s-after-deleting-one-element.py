class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_count = 0
        left = 0
        largest_window_of_ones = 0
        
        # First check the number of zeros in a given window
        for right in range(len(nums)):
            zero_count += 1 if nums[right] == 0 else 0
            
            ''' 
            Shrink the window form the left whenever the number of zeros exceed 1
            Reduce the number of zeros by 1, to keep the number of zeros at the limit 1,
            the moment another zero is found by the right pointer
            '''
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            '''
            Subtract the left pointer value from the current value of the right pointer.
            This makes it look like we have deleted one zero from the subarray.
            Now find the maximum window of ones
            '''
            current_window_of_ones = right - left
            largest_window_of_ones = max(largest_window_of_ones, current_window_of_ones)
        
        return largest_window_of_ones
    
            