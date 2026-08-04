class Solution:
    @staticmethod
    def generate(numRows: int) -> list[list[int]]:
        result = [[1],[1,1]]
        if numRows == 1:
            result = [[1]]
            return result
        elif numRows == 2:
            return result
        else:
            for i in range(2, numRows):
                new_item = [1,1]
                for item in range(len(result[-1])-1):
                    new_item.insert(item + 1, result[-1][item] + (result[-1][item+1])) 
                result.append(new_item)
            return result