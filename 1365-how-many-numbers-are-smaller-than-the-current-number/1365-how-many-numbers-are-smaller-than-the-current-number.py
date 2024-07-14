class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        max_val = max(nums)
        freq = [0] * (max_val + 1)
        result = []
        
        # Frequency array to count number of times a number occurs in nums
        # The number in nums is represented by the index and the count is the
        # number in that index
        
        for num in nums:
            freq[num] += 1
        
        # Frequency array is used to create a prefix sum array 
        for i in range(1, len(freq)):
            freq[i] += freq[i - 1]
        
        # The element before index of num in the prefix sum array 
        # serves as the number of elements in nums list that are lesser than num

        for num in nums:
            if num == 0:
                result.append(0) # to handle index out of range exception
            else:
                result.append(freq[num - 1])
        return result
