import math

class Solution:


    def findRoot(self, nums: list[int]):
        if len(nums) % 2 != 0:
            root = int(math.ceil(len(nums)/2) - 1)
        else:
            root = (len(nums)/2 - 1)
        
        return int(root)

    def search(self, nums: list[int], target: int) -> int:
        count = -1
        while nums:
            root = self.findRoot(nums= nums)
            if target == nums[root]:
                count += root + 1
                return count
                break
            elif target > nums[root]:
                count += root + 1
                nums = nums[(root)+1:]
            elif target < nums[root]:
                nums = nums[:(root)]
        return -1
solution = Solution()

print(solution.search(nums=[-1,0,3,5,9,12],target=9))