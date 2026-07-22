class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        if k == len(blocks):
            count = Counter(blocks)
            return count['W'] 
        l, r = 0, k
        minimum = float('inf')

        while r < len(blocks):
            count = Counter(blocks[l:r])
            print(blocks[l:r])
            count_b = count['B']
            minimum = min(len(blocks[l:r]) - count_b, minimum)
            l += 1
            r += 1
        return minimum

