class Solution:

    def encode(self, strs: list[str]) -> str:
        result = ''
        for item in strs:
            result += item
            result += "salt"
        return result

    def decode(self, s: str) -> list[str]:
        s = s.split("salt")
        if s[-1] == '':
            s.pop() 
        return s