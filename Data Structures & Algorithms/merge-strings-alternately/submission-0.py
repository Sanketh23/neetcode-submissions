class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        r = 0
        word3 = ""
        maxLen = max(len(word1), len(word2))

        for i in range(maxLen):
            if l > (len(word1) - 1):
                word3 += word2[r:]
                break
            elif r > (len(word2) - 1):
                word3 += word1[l:]
                break
            else:
                word3 += word1[l]
                word3 += word2[r]
                l += 1
                r += 1
        return word3
