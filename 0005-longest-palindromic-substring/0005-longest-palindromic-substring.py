class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_str = len(s)
        longest_pal = ""
        reversed_str = s[::-1]

        # loop through first in range(len)
        for first in range(len_str):
            if len(longest_pal) > (len_str - first):
                return longest_pal
            for last in reversed(range(len_str)):
                if s[first] == s[last]:
                    curr_str = s[first:last + 1]
                    curr_reversed = reversed_str[len_str - (last + 1):(len_str - first)]
                    if curr_str == curr_reversed:
                        if len(curr_str) > len(longest_pal):
                            longest_pal = curr_str

        return longest_pal