class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000, 
        }
        nums = []
        for char in s[::-1]:
            if len(nums) == 0:
                nums.append(romans[char])
            elif nums[-1] > romans[char]:
                nums[-1] = nums[-1] - romans[char]
            else:
                nums.append(romans[char])
        return sum(nums)