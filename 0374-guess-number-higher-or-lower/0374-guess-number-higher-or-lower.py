# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n + 1
        while True:
            mid = (left + right) // 2
            pick = guess(mid)
            if pick > 0:
                left = mid + 1
            elif pick < 0:
                right = mid - 1
            else:
                return mid
                