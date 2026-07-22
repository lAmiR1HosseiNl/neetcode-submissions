class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        count_zero = nums.count(0)
        multi = 1
        for num in nums:
            if num != 0:
                multi = multi * num
        for i in range(len(nums)):
            if count_zero>1:
                result.append(0)
            elif count_zero == 1:
                if nums[i] == 0:
                    result.append(int(multi))
                else:
                    result.append(0)
            else:
                result.append(int(multi/nums[i]))
        
        return result