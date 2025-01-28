class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = {}
        ans = {}
        for c in p:
            if c not in ans:
                ans[c] = 1
            else:
                ans[c] += 1
        needs = len(ans.keys())
        result = []
        curr = 0
        for i, c in enumerate(s):
            if i >= len(p):
                prev = True if s[i-len(p)] in ans and count[s[i-len(p)]] == ans[s[i-len(p)]] else False
                count[s[i-len(p)]] -= 1
                if s[i-len(p)] in ans and count[s[i-len(p)]] == ans[s[i-len(p)]]:
                    curr += 1
                elif prev:
                    curr -= 1

            prev = True if c in ans and c in count and count[c] == ans[c] else False    
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1

            if c in ans and count[c] == ans[c]:
                curr += 1
            elif prev:
                curr -= 1

            if i >= len(p)-1 and curr == needs:
                result.append(i-len(p)+1)
        return result
            