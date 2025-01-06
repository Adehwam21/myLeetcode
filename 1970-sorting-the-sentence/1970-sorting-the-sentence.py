class Solution:
    def sortSentence(self, s: str) -> str:
        s = sorted(s.split(" "), key = lambda word: int(word[-1]))
        sentence = ""
        for word in s:
            sentence += word[:len(word)-1] + " "
        
        return sentence.strip()



        