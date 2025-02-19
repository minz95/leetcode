class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']
        if k > 3 * 2**(n-1):
            return ""

        result = []
        k -= 1
        first_idx = k // (2**(n-1))
        result.append(letters[first_idx])
        k %= (2 ** (n-1))

        for i in range(n-1):
            prev = result[-1]
            candidates = [c for c in "abc" if c != prev]
            idx = k // (2 ** (n-i-2)) if n-i-2 >= 0 else 0
            result.append(candidates[idx])
            k %= (2 ** (n-i-2)) if n-i-2 >= 0 else 0
        return "".join(result)  