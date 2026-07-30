class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Ans = []
        len1 = len(nums)
        for i in range(len1):
            for j in range (i+1,len1):
                if (nums[i]+nums[j]) == target:
                    Ans.append(i)
                    Ans.append(j)
                else:
                     pass
        return Ans