class Solution:
    @staticmethod
    def longestCommonPrefix(strs: list[str]) -> str:
        min_len_item = min(strs,key=len)
        min_prefix = ''
        for word in strs:
            new_word = ''
            for char in range(len(min_len_item)):
                if word == strs[0]:
                    if word[char] == min_len_item[char]:
                        new_word += (min_len_item[char])
                    else:
                        min_prefix = new_word          
                        break         
                else:
                    if word[char] == min_len_item[char]:
                        new_word += (min_len_item[char])
                    else:
                        min_prefix = min(min_prefix, new_word, key=len)
                        break
            if word == strs[0]:
                min_prefix = new_word
            else:
                min_prefix = min(min_prefix, new_word, key=len)

        return (min_prefix)            