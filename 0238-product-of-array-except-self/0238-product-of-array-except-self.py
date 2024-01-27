class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        arr_length = len(nums)
        answer = [1] * arr_length
        
        for i in range(arr_length):
            answer[i] = prefix
            prefix *= nums[i]
        
        for i in range(arr_length-1,-1,-1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
            
        