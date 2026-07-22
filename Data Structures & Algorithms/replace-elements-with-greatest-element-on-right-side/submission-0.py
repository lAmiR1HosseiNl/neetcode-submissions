class Solution:
    @staticmethod
    def replaceElements(arr: list[int]) -> list[int]:
        for i in range(len(arr)):
            if i+1 == len(arr):
                arr[-1] = -1
            else:
                arr[i] = max(arr[i+1::])
        return arr
