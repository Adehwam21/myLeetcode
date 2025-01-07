class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        match = {}

        for word1 in words:
            for word2 in words:
                if word1 not in match and len(word1) < len(word2):
                    if word1 in word2:
                        match[word1] = word2
        return list(match.keys())
