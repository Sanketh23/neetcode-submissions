class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            res = 0
            while i:
                if i & 1:
                    res += 1
                i >>= 1
            output.append(res)
        return output
        