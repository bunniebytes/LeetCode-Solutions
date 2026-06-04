class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        count = 0
        for num in range(num1, num2 + 1):
            num, prev = divmod(num, 10)
            num, curr = divmod(num, 10)
            while num > 0:
                num, _next = divmod(num, 10)
                if (curr > prev and curr > _next) or (curr < prev and curr < _next):
                    count += 1
                prev = curr
                curr = _next
        return count