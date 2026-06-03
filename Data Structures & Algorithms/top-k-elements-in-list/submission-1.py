class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        res = []
        for num, freq in sorted_count.items():
            res.append(num)
            if len(res) == k:
                break
        return res