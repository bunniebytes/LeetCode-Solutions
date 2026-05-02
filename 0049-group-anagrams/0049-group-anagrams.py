class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        # we know all anagrams have same keys
        # sorted_string_list = sort each of the strings in the list
        # create a dictionary of those unique keys and list strs[index] (enumerate)
        for _str in strs:
            anagram_dict[("").join(sorted(_str))].append(_str)
        return list(anagram_dict.values())
        # return dictionary.values() have to figure out syntax to add them to a list (list of lists)