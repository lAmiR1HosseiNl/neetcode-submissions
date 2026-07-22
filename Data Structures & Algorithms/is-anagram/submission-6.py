class Solution:

    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        if len(s) == len(t):
            if (sorted(list(t)) == sorted(list(s))):
                return True
            else: 
                return False
        else:
            return False
