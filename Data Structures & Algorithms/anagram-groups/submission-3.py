class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        Ans = []
        for i in range(len(strs)):
            if len(strs) == 1 and Ans:
                if Ans[-1] != strs:
                    Ans.append(strs)
            elif len(strs) == 1:
                Ans.append(strs)
                return Ans
            else:
                List1 = []
                for j in range(len(strs)):
                    if self.isAnagram(strs[i],strs[j]):
                        List1.append(strs[j])
                    else:
                        pass
                if List1 and List1 not in Ans:
                    Ans.append(List1)

        return (Ans)

    def isAnagram(self,main_word:str,check_word:str)->bool:
        check_word = list(check_word)
        main_word  =  list(main_word)
        result = True
        if(len(check_word) == len(main_word)):
            for word in main_word:
                if word in check_word:
                    check_word.remove(word)
                else:
                    result = False
            return result