class Solution:
    @staticmethod
    def scoreOfString(s: str) -> int:
        list_s = list(s)
        sum = 0
        for i in range(1,len(list_s)):
            sum += abs(ord(list_s[i]) - ord(list_s[i-1]))

        return sum