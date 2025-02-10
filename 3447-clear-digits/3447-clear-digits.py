class Solution:
    def clearDigits(self, s: str) -> str:
        non_digit = []
        for c in s:
            if '0' <= c <= '9':
                if non_digit:
                    non_digit.pop()
            else:
                non_digit.append(c)
        return "".join(non_digit)