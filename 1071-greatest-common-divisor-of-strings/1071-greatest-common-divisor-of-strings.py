class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_length = len(str1)
        str2_length = len(str2)
        
        def isDivisor(length: int):
            if str1_length % length or str2_length % length:
                return False
            factor1 = str1_length // length
            factor2 = str2_length // length
            return (str1 == str1[: length] * factor1) and (str2 == str1[: length] * factor2)
        
        for length in range(min(str1_length, str2_length), 0, -1):
            if isDivisor(length):
                return str1[:length]
        return ""
        