class Solution:
    @staticmethod
    def isSubsequence(s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        placment_list = [-1]

        if len(list_s) > len(list_t):
            return False
        elif len(list_s) < len(list_t):
            try:
                for item in list_s:
                    placment_list.append(list_t.index(item, placment_list[-1]+1))
            except:
                return False
            if placment_list == sorted(placment_list):
                return True
            else:
                return False
        else:
            try:
                for item in list_s:
                    placment_list.append(list_t.index(item, placment_list[-1]+1))
            except:
                return False
            if placment_list == sorted(placment_list):
                return True
            else:
                return False