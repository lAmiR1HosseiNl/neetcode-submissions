class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        stack = []
        hashMap = {"(":")", "[":"]", "{":"}"}
        for item in range(len(s)):
            if s[item] in hashMap:
                stack.append(s[item])
            elif (s[item]) and (s[item] in hashMap.values()):
                try:
                    if hashMap.get(stack[-1]) == s[item]:
                        stack.pop(-1)
                    else:
                        return False
                except:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False