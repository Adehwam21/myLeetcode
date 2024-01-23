class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        # Find the greatest number
        greatest = max(candies)
        
        # Check if the sum of the number in the ith position and extraCandies
        # will be greater than the maximum number in the list.
        # Convert the item in the ith position to True if the check is valid and 
        # False otherwise
        
        for i in range(0, len(candies)):
            if candies[i] + extraCandies >= greatest:
                candies[i] = True
            else:
                candies[i] = False
        return candies  