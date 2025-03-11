class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        i, j = 0, 1
        count = {'a': 0, 'b': 0, 'c':0}
        satisfy_cnt = 0
        count[s[i]] += 1
        satisfy_cnt += 1
        total = 0

        while j < len(s):
            count[s[j]] += 1
            if count[s[j]] == 1:
                satisfy_cnt += 1
            while satisfy_cnt == 3 and j - i >= 2:
                total += len(s) - j
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    satisfy_cnt -= 1
                i += 1
            j += 1
        return total