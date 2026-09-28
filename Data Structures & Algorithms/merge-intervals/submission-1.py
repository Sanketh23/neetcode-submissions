class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(int)
        for start, end in intervals:
            hashmap[start] += 1
            hashmap[end] -= 1

        res = []
        interval = []
        have = 0

        for i in sorted(hashmap):
            if not interval:
                interval.append(i)
            have += hashmap[i]
            if have == 0:
                interval.append(i)
                res.append(interval)
                interval = []
        return res