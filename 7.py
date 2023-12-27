class Solution:
    def reverse(self, x: int) -> int:
        answer = 0
        isNegative = False

        if x < 0:
            isNegative = True
            x = -x

        while x != 0:
            answer = (answer * 10) + (x % 10)
            x //= 10

        if isNegative:
            answer = -answer

        if answer > 2**31 - 1 or answer < -2**31:
            return 0

        return answer

