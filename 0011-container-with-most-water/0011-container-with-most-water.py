class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        all_area = []
        area = 0
        
        while left <= (len(height)-1) and right >= 0:
            if height[left] <= height[right]:
                area = height[left] * (left-right)
                all_area.append(area)
                left += 1
                
            elif height[right] < height[left]:
                area = height[right] * (right-left)
                all_area.append(area)
                right -= 1
        all_area = [abs(area) for area in all_area]
        print(all_area)
        return max(all_area)
                
                
        