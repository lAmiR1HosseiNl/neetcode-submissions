class Solution:
    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        dictionry_of_convert = dict()
        seen = set()
        if len(s) == len(t):
            for i in range(len(s)):
                if t[i] not in (dictionry_of_convert.values()):
                    dictionry_of_convert[(s[i]).lower()] = (t[i]).lower()
        else:
            return False
        new_s = ''
        try:
            for i in range(len(s)):
                new_s += dictionry_of_convert[(s[i]).lower()]
            print(dictionry_of_convert)
            if (new_s) == (t).lower():
                return True
            else:
                return False
        except:
            return False