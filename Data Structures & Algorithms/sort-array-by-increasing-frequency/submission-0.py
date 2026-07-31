class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        def sort_key(n):
            return (count[n], -n)
        
        nums.sort(key=sort_key)
        return nums