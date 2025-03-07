class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        d = [0] * (right + 1)
        d[0] = d[1] = 1
        for num in range(2, int(right**0.5) + 1):
            if d[num] == 0:
                for j in range(num * num, right + 1, num):
                    d[j] = 1
        primes = [num for num in range(left, right + 1) if d[num] == 0]

        if len(primes) < 2:
            return -1, -1
        min_diff = float('inf')
        pair = (-1, -1)

        for i in range(1, len(primes)):
            diff = primes[i] - primes[i-1]
            if diff < min_diff:
                min_diff = diff
                pair = primes[i-1], primes[i]
        return pair