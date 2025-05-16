class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2 != 0:
            return False
        set_divisors = {1}
        highest_divisor = int(num / 2)
        set_divisors.add(2)
        set_divisors.add(highest_divisor)
        for x in range(3, highest_divisor, 1):
            y = num / x
            if y in set_divisors:
                break
            if num % x == 0:
                set_divisors.add(x)
                set_divisors.add(y)
        if sum(set_divisors) == num:
            return True
        else:
            return False
        