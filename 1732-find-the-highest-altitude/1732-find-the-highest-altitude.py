class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        point_altitude = [0] * (len(gain)+1)
        
        for i in range(1, len(gain)+1):
            point_altitude[i] = point_altitude[i-1] + gain[i-1]    
        return max(point_altitude)
    