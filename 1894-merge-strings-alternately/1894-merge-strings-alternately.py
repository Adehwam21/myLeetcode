class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        temp = []
        i = 0
        j = 0
        
        while i < len(word1) and j < len(word2):
            temp.append(word1[i])
            temp.append(word2[j])
            i+=1
            j+=1
            
        temp.append(word1[i:])
        temp.append(word2[j:])
        return "".join(temp)