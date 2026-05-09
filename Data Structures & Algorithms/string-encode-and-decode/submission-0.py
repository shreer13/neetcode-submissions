class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for item in strs:
            L = len(item)
            res += str(L) + "#" + item
        return res
            

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            #FInd delimiter
            j = s.find("#",i)

        #FInd length
            L = int(s[i:j])

            res.append(s[j+1:j+1+L])

            i = j+ 1+L
        return res