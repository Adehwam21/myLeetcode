class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cleaned = s.strip(" ")
        cleaned = [i for i in cleaned]
        new = cleaned[::-1]
        new1 =[]
        for i in range(len(new)):
            if len(new[i]) == 1:
                new1.append(new[i])
                if new[i] == str(" "):
                    new1.pop(i)
                    break
            else:
                i+=1

        return (len(new1))
