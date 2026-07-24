class Solution:
    def minOperations(self, s: str) -> int:
        current = 0
        count1 = 0
        for char in s:
            if int(char) != current:
                count1 += 1
            current ^= 1
        current = 1
        count2 = 0
        for char in s:
            if int(char) != current:
                count2 += 1
            current ^= 1
        return min(count1, count2)
        

