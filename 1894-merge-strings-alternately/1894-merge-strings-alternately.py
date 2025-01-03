class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_word = min(len(word1), len(word2))
        alt_word = ""
        for i in range(min_word):
            alt_word += word1[i] + word2[i]
        
        if len(word1) > len(word2):
            alt_word += word1[min_word:]
        elif len(word2) > len(word1):
            alt_word += word2[min_word:]
        
        return alt_word
        