class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i=0
        list1 = []
        Ans = False
        for item in nums:
            if item in list1:
                Ans = True
            else:
                list1.append(item)
        return Ans


