class Solution:
    @staticmethod
    def removeElement(nums: list[int], val: int) -> int:
        count = 0
        len_nums = len(nums)
        for i in range(len_nums):
            if val in nums:
                nums.remove(val)
                count += 1
        val = len_nums - count
        return val