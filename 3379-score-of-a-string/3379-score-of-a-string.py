class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = None
        ascii_list = []
        _sum = 0
        for letter in s:
            if prev is None:
                prev = ord(letter)
            else:
                curr = ord(letter)
                _sum += abs(prev - curr)
                prev = curr
        return _sum
        
