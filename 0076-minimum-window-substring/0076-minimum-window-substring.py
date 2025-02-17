from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = Counter(t)
        correct = 0
        target = len(count.keys())
        chmap = {s[0]: 1}
        minwin = ""
        if s[0] in count and count[s[0]] == 1:
            correct += 1
        if len(t) == 1 and correct == target:
            return t
        i = 0
        for j in range(1, len(s)):
            if s[j] in chmap:
                chmap[s[j]] += 1
            else:
                chmap[s[j]] = 1
            
            if s[j] in count and count[s[j]] == chmap[s[j]]:
                correct += 1
            if correct == target:
                while (s[i] not in count or chmap[s[i]] > count[s[i]]) and i < j:
                    chmap[s[i]] -= 1
                    i += 1
                if minwin == "" or len(minwin) > j - i + 1:
                    minwin = s[i:j+1]
        return minwin
