class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        result = []
        for i, c in enumerate(s):
            if i == 0:
                if c in wordDict:
                    result.append(True)
                else:
                    result.append(False)
            else:
                possible = False
                for j in range(i, -1, -1):
                    if j == 0:
                        if s[:i+1] in wordDict:
                            possible = True
                    elif s[j:i+1] in wordDict and result[j-1]:
                        possible = True
                        break
                result.append(possible)
        return result[-1]