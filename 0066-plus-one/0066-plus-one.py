class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        result = []

        for i in range(len(digits)-1, -1, -1):
            v = digits[i] + carry
            if v >= 10:
                carry = 1
                v = v - 10
            else:
                carry = 0
            result.append(v)
        if carry == 1:
            result.append(carry)
        return result[::-1]
                