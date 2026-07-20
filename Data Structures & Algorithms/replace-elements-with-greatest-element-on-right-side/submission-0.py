class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr) - 1, -1, -1):
            temp = rightMax
            rightMax = max(rightMax, arr[i])
            arr[i] = temp

        return arr

