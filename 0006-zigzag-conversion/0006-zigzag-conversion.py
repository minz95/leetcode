class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        down = False
        curr = 0
        rows = [''] * numRows

        for c in s:
            rows[curr] += c
            if curr == 0 or curr == numRows - 1:
                down = not down
            curr += 1 if down else -1

        return ''.join(rows)
