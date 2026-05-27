class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower_set = set()
        upper_map = {}
        result = 0

        for letter in word:
            if letter.islower():
                lower_set.add(letter)
                upper_check = upper_map.get(letter.upper())
                if upper_check:
                    upper_map[letter.upper()] = False
                    result -= 1
            if letter.isupper():
                if letter.lower() in lower_set and letter not in upper_map:
                    upper_map[letter] = True
                    result += 1
                if letter.lower() not in lower_set:
                    upper_map[letter] = False

        return result