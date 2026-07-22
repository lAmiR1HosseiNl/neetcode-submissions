class Solution:
    @staticmethod
    def hasDuplicate(nums: list[int]) -> bool:
        if(nums):
            num_check = nums.copy()
            for item in nums:
                num_check.remove(item)
                if (num_check):
                    if (item in num_check):
                        return True
                else:
                    return False
        else:
            return False