# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def bina(num):
            decimal = 0
            for digit in str(num):
                decimal = decimal * 2 + int(digit)
            return decimal

        a = bina(a)
        b = bina(b)
        c = a + b

        def out(c):
            return bin(c)[2:]

        return out(c)
