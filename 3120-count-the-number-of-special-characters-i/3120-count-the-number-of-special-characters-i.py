class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upper_set = set()
        lower_set = set()
        for letter in word:
            if letter.isupper():
                upper_set.add(letter.lower())
            else:
                lower_set.add(letter)

        return len(upper_set & lower_set)