class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        w = n - k

        minsum = currsum = sum(cardPoints[:w])
        for i in range(w, n):
            currsum += cardPoints[i] - cardPoints[i-w]
            minsum = min(minsum, currsum)
        return total - minsum