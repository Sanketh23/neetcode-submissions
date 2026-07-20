class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonMap = defaultdict(int)
        for char in text:
            if char in ['b','a','l','o','n']:
                balloonMap[char] += 1
        
        balloonMap['l'] //= 2
        balloonMap['o'] //= 2
        return min(balloonMap.values())