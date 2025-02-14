import math
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7
        l = a // math.gcd(a, b) * b

        s = 1
        e = n * min(a, b)
        while s < e:
            m = (s + e) // 2
            if m//a + m//b - m//l < n:
                s = m + 1
            else:
                e = m
        return s % MOD
