class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        diff_count = 0
        diff_index = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_count += 1
                diff_index.append(i)

        return diff_count == 2 and s1[diff_index[0]] == s2[diff_index[1]] and s1[diff_index[1]] == s2[diff_index[0]]