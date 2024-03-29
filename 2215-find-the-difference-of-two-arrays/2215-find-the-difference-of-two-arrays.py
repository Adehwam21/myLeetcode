class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        a, b = [], []
        
        disjoint = nums1.symmetric_difference(nums2)
        
        for i in disjoint:
            if i in nums1:
                a.append(i)
            else:
                b.append(i)
        return ([a,b])
            
        
        