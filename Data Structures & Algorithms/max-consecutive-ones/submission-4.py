class Solution:
    @staticmethod
    def findMaxConsecutiveOnes(nums: list[int]) -> int:
        zero_placement = []
        starter = -1
        try:
            for _ in nums:
                zero_placement.append(nums.index(0,starter+1))
                starter = zero_placement[-1]
        except:
            pass
        finally:
            if nums[-1] != 0:
                zero_placement.append(len(nums))

        result = zero_placement[0]
        for i in range(len(zero_placement)-1):
            result = max(result, (zero_placement[i+1] - zero_placement[i]-1))

        return (result)