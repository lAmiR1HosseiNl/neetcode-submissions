class Solution:
    @staticmethod
    def lengthOfLastWord(s: str) -> int:
        s = (s.split(" "))
        s = list(filter(None, s))
        return len(s[-1])