class Solution:
    def lcs(self, str1, str2):
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        dp = self.lcs(str1, str2)
        m, n = len(str1), len(str2)
        
        i, j = m, n
        scs = []

        # LCS 테이블을 역추적하면서 SCS 구성
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:  # 공통 문자 -> SCS에 추가
                scs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:  # str1의 문자가 더 중요
                scs.append(str1[i - 1])
                i -= 1
            else:  # str2의 문자가 더 중요
                scs.append(str2[j - 1])
                j -= 1

        # 남은 문자열 추가 (한쪽 문자열이 끝나면 남은 부분 붙이기)
        while i > 0:
            scs.append(str1[i - 1])
            i -= 1
        while j > 0:
            scs.append(str2[j - 1])
            j -= 1

        return "".join(reversed(scs))
                