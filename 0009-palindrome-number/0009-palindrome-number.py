class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_num = x % 10
        num = int(x / 10)
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        while num != 0:
            rev_num = rev_num * 10 + num % 10
            num = int(num / 10)
        return x == rev_num