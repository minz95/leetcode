from collections import defaultdict
class Solution:
    def numSplits(self, s: str) -> int:
        m1 = {}
        m2 = {}
        count = 0
        m1[s[0]] = 1
        for i in range(1, len(s)):
            if s[i] in m2:
                m2[s[i]] += 1
            else:
                m2[s[i]] = 1
        if len(m1.keys()) == len(m2.keys()):
            count += 1

        for i in range(2, len(s)):
            c = s[i-1]
            if c in m1:
                m1[c] += 1
            else:
                m1[c] = 1
            m2[c] -= 1
            if m2[c] == 0:
                del m2[c]
            if len(m1.keys()) == len(m2.keys()):
                count += 1
        return count
