class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        # split words into list of sets (not worried about how many times it shows up)
        word_list = text.split()
        count = 0

        for word in word_list:
            temp = False
            word = set(word)
            for letter in brokenLetters:
                if letter in word:
                    temp = True
                    break
            if not temp:
                count += 1

        return count