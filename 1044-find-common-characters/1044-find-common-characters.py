class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = [0]*26
        current = [0]*26
        result = []

        for char in words[0]:
            common[ord(char) - ord('a')] += 1
        
        for word in words[1:]:
            current = [0] * 26
            for char in word:
                letter_pos = ord(char) - ord('a')
                current[letter_pos] += 1

            for letter in range(len(common)):
                common[letter] = min(
                    common[letter],
                    current[letter]
                )
            
        for letter_pos, count in enumerate(common):
            for freq in range(count):
                result.append(chr(ord('a') + letter_pos))
        
        return result
        