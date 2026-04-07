class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) > len(word2):
            iteration = len(word1)
        else:
            iteration = len(word2)

        storage = []
        i, j = 0, 0
       
        while i<len(word1) and j<len(word2):
            storage.append(word1[i])
            storage.append(word2[j])
            i+=1
            j+=1
        while i<len(word1):
            storage.append(word1[i])
            i+=1
        while j<len(word2):
            storage.append(word2[j])
            j+=1
        return "".join(storage)
