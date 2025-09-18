class Solution(object):
    def longestCommonPrefix(self, strs):
        strs = list(set(strs))
        prefix = strs[-1]

        for word in strs:
            index = 0
            while index < len(prefix) and index < len(word) and prefix[index] == word[index]:
                index += 1
            prefix = prefix[:index]
            if len(prefix) == 0:
                return prefix
        return prefix