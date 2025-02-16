class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        size = (n - 1) * 2 + 1
        s = [0] * size
        used = set()

        def backtrack(idx):
            nonlocal s
            if idx == size:
                return True
            if s[idx] != 0:
                return backtrack(idx + 1)
            for i in range(n, 0, -1):
                if i in used:
                    continue

                if i == 1:
                    s[idx] = i
                    used.add(i)
                    if backtrack(idx + 1):
                        return True
                    s[idx] = 0
                    used.remove(i)
                else:
                    if idx + i < size and s[idx + i] == 0:
                        s[idx] = s[i + idx] = i
                        used.add(i)
                        if backtrack(idx + 1):
                            return True
                        s[idx] = s[i + idx] = 0
                        used.remove(i)
            return False

        backtrack(0)
        return s