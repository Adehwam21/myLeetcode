class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split(" ")
        sentence = [""] * len(s)
        sorted_sentence = ""

        for word in s:
            idx = int(word[-1])-1
            sentence[idx] = word[:len(word)-1]
        
        for word in sentence:
            sorted_sentence += word + " "
        
        return sorted_sentence.strip()


        