class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if ((str(int(target) - 1) in deadends and str(int(target) + 1) in deadends)  and (str(int(target) - 10) in deadends and str(int(target) + 10) in deadends) and (str(int(target) - 100) in deadends and str(int(target) + 100) in deadends) and (str(int(target) - 1000) in deadends and str(int(target) + 1000) in deadends)):
            return -1
        
        count = 0
        for num in target:
            count += min(10 - int(num), int(num) - 0)
        return count