class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        visited = set()
        visited.add(beginWord)
        q = deque([(beginWord, 1)])
        
        while q:
            word, pathLen = q.popleft()
            for i in range(len(word)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if char == word[i]:
                        continue
                    candidate = word[:i] + char + word[i+1:]
                    if candidate == endWord:
                        return pathLen + 1
                    if candidate in wordSet and candidate not in visited:
                        visited.add(candidate)
                        q.append((candidate, pathLen + 1))
        
        return 0