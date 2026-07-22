class Solution:
    @staticmethod
    def hasDuplicate(nums: list[int]) -> bool:
        if(len(nums) == len(set(nums))):
            return False
        else:
            return True

print(Solution.hasDuplicate([1, 2, 3, 4]))