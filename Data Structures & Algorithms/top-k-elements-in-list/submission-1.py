class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        List_count = []
        List_nums = []
        result = []
        f_result = []
        for i in range(len(nums)):
            item = nums[i]
            if item not in List_nums:
                List_nums.append(nums[i])
                
        for item in List_nums:
            count = 0
            for items in nums:
                if item == items:
                    count += 1
            List_count.append(count)
        zips = list(zip (List_nums,List_count))
        sorted_data = sorted(zips, key=lambda x:x[1] ,reverse=True)
        for item in range (k):
            result.append(sorted_data[item])
        for m in range(len(result)):
            f_result.append(result[m][0])    
        return f_result