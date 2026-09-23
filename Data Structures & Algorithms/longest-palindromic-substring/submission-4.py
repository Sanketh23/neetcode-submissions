class Solution:
    def longestPalindrome(self, s: str) -> str:
        queue = deque([s])
        while queue:
            res = queue.popleft()
            if res == res[::-1]:
                return res
            queue.append(res[1:])
            queue.append(res[:len(res)-1])
            queue.append(res[1:])
            queue.append(res[:len(res)-1])
        

