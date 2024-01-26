class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        all_area = []
        area = 0
        
        while left <= (len(height)-1) and right >= 0:
            if height[left] <= height[right]:
                area = height[left] * (right-left)
                all_area.append(area)
                left += 1
                
            elif height[right] < height[left]:
                area = height[right] * (right-left)
                all_area.append(area)
                right -= 1
        return max(all_area)
                