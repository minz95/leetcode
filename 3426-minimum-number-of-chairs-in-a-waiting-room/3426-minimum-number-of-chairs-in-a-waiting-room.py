class Solution:
    def minimumChairs(self, s: str) -> int:
        count = 0
        max_cnt = 0
        for c in s:
            if c == 'E':
                count += 1
            elif c == 'L':
                count -= 1
            max_cnt = max(count, max_cnt)
        return max_cnt
        