class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        word1_map = Counter(word1)
        word2_map = Counter(word2)
        
        word1_char_freq = Counter([a for a in word1_map.values()])
        word2_char_freq = Counter([b for b in word2_map.values()])
        
        return word1_map == word2_map or (word1_char_freq == word2_char_freq and set(word1) == set(word2))
    