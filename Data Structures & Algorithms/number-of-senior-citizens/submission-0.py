class Solution:
    @staticmethod
    def countSeniors(details: list[str]) -> int:
        count_greater_than_60 = 0
        for item in range(len(details)):
            if int(details[item][11:13]) > 60:
                count_greater_than_60 += 1
        
        return (count_greater_than_60)