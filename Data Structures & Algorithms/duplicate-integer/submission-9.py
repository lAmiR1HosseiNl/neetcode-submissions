class Solution:
    @staticmethod
    def hasDuplicate(nums: list[int]) -> bool:
        if(len(nums) == len(set(nums))):
            return False
        else:
            return True
