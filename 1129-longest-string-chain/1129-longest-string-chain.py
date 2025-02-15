class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        max_length = 1

        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                prev = w[:i] + w[i+1:]
                if prev in dp:
                    dp[w] = max(dp[w], dp[prev] + 1)
            max_length = max(max_length, dp[w])

        return max_length