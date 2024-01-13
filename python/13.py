class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = []
        s = reversed(s)

        for i in s:
            if i == 'I':
                numbers.append(1)

            if i == 'V':
                numbers.append(5)

            if i == 'X':
                numbers.append(10)

            if i == 'L':
                numbers.append(50)

            if i == 'C':
                numbers.append(100)

            if i == 'D':
                numbers.append(500)

            if i == 'M':
                numbers.append(1000)

        answer = numbers[0]

        for i in range(1, len(numbers)):
            next = numbers[i]

            if next < numbers[i - 1]:
                next = -next

            answer += next

        return answer

