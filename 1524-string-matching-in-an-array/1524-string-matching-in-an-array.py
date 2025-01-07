class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        match = []
        for word1 in words:
            for word2 in words:
                if word1 in word2 and len(word1) < len(word2) and word1 not in match:
                    match.append(word1)
        
        return match