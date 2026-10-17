class Solution:
    def mySqrt(self, x: int) -> int:
        a = x
        if x <= 0: 
            return 0

        while True:
            nextX = 0.5 * (x + a / x)
            if abs(nextX - x) < 0.0000001 :
                return int(nextX)
            x = nextX