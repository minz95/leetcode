class Solution:
    def lenLongestFibSubseq(self, arr):
        index_map = {num: i for i, num in enumerate(arr)}
        n = len(arr)
        dp = defaultdict(lambda: 2)  # 기본값 2 (최소 길이 3 이상 필요)
        max_len = 0

        for k in range(n):
            for j in range(k):
                i = index_map.get(arr[k] - arr[j])
                if i is not None and i < j:  # 유효한 피보나치 관계인지 확인
                    dp[j, k] = dp[i, j] + 1
                    max_len = max(max_len, dp[j, k])

        return max_len if max_len >= 3 else 0  # 최소 길이 3 이상