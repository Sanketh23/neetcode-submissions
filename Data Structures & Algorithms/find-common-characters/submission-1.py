class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])

        for word in words:
            curr = Counter(word)
            for c in count:
                count[c] = min(count[c], curr[c])

        res = []
        for c in count:
            res.extend(count[c] * c)
            
        return res
