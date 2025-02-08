class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        s, e = 0, len(xstr) - 1
        while s <= e:
            if xstr[s] != xstr[e]:
                return False
            s += 1
            e -= 1
        return True