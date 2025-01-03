class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Get the mininum string in the array
        lengths = [len(string) for string in strs]
        min_str = min(lengths)
        min_str_index = lengths.index(min_str)
        longest_common_prefix = ""
        
        for i in range(min_str):
            for string in strs:
                if string[i] != strs[min_str_index][i]:
                    return longest_common_prefix
                
            longest_common_prefix += string[i]
        
        return longest_common_prefix
                