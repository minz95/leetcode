class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        idx = 0
        w = 0
        while w < len(s):
            c = s[w]
            if c != part[idx] and idx > 0:
                w = w - idx + 1
                idx = 0
            if c == part[idx]:
                idx += 1
            if idx == len(part):
                s = s[:w-len(part)+1] + s[w+1:]
                w = max(0, w-2*len(part)+2)
                idx = 0
            else:
                w += 1
        return s