class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_dict = {"I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000}
        prev = None
        ans = 0

        for x in s:
            curr = roman_int_dict[x]
            if prev is None:
                prev = roman_int_dict[x]
                ans = prev
            else:
                if prev >= curr:
                    prev = curr
                    ans += prev
                elif prev < curr:
                    ans = ans + curr - 2*prev
                    prev = curr - prev
                    
        return ans
