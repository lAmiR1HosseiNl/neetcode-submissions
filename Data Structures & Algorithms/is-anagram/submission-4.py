class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Ans = True
        T = list(t)
        for item in s:
            if item in T and len(s) == len(t):
                T.remove(item)
            else:
                Ans = False
        return Ans
