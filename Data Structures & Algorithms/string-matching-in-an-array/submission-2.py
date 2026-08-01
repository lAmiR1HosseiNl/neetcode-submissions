class Solution:
    @staticmethod
    def stringMatching(words: list[str]) -> list[str]:
        result = []
        len_words = len(words)
        for _ in range(len_words):
            current_min_word = min(words,key=len)
            words.remove(current_min_word)
            for item in words:
                sub_sets_of_word = []
                for char in range(len(item)-len(current_min_word)+1):
                    sub_sets_of_word.append(item[char:char+len(current_min_word)])
                if ((current_min_word in sub_sets_of_word) & (current_min_word not in result)):
                    result.append(current_min_word)
                    
        return result