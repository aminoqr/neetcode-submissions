class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            n = len(word)
            res += str(n) + "@" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            l = 0
            while s[i].isdigit():
                l  = l * 10 + int(s[i])
                i+=1
            res.append(s[i+1:i+l+1])
            i += l + 1
        
        return res