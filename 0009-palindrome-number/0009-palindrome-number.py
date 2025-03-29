class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_x = list(str(x))
        if x >= 0:
            reverse_x = list_x[::-1]
            if reverse_x == list_x:
                return True
            else:
                return False
        return False