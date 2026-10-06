class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        area = 0

        while l <= (len(height)-1) and r >= 0:
            if height[l] <= height[r]:
                A = height[l] * (r-l)
                area = A if A > area else area
                l += 1
            else:
                A = height[r] * (r-l)
                area = A if A > area else area
                r -= 1
        return area
                