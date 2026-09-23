class Solution:
    def longestPalindrome(self, s: str) -> str:
        queue = deque([(s,None)])
        while queue:
            res, prev = queue.popleft()
            if res == res[::-1]:
                return res
            if prev == None:
                queue.append((res[1:], "left"))
                queue.append((res[:len(res)-1], "right"))
            elif prev == "right":
                queue.append((res[1:], "left"))
            else:
                queue.append((res[:len(res)-1], "right"))
        

