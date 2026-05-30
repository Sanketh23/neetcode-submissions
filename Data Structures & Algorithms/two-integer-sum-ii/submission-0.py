class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1
        while l < r:
            sumPointers = numbers[l] + numbers[r]
            if sumPointers == target:
                return [numbers[l],numbers[r]]
            elif sumPointers < target:
                l += 1
            else:
                r -= 1
        


