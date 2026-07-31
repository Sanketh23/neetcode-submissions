class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1, str2):
            length = len(str1)
            if str1 == str2[0:length] and str1 == str2[len(str2) - length:len(str2)]:
                
                return True
        res = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    if i < j:
                        res += 1
        return res

