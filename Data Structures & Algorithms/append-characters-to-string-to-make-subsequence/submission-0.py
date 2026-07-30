class Solution:
    @staticmethod
    def appendCharacters(s: str, t: str) -> int:
        list_s = list(s)
        list_t = list(t)
        result_list = [0] * len(list_t)
        starter = -1
        counter = 0
        for item in t:
            try:
                if isinstance(list_s.index(item, starter + 1),int):
                    result_list[counter] = 1
                    starter = list_s.index(item, starter + 1)
                else:
                    pass
            except:
                pass

            counter += 1
        try:
            number_zero = result_list.index(0)
            number_to_add = len(result_list) - number_zero
        except:
            number_to_add = 0
        
        return number_to_add