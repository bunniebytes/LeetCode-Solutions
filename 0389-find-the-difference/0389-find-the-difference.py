class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = {char : s.count(char) for char in set(s)}
        t_dict = {char : t.count(char) for char in set(t)}
        s_keys = set(s_dict.keys())
        t_keys = set(t_dict.keys())
        # check len of keys for both - if not equal return the extra
        if len(s_keys) != len(t_keys):
            return t_keys.difference(s_keys).pop()
        # check if value for both are same - if not we would return key
        for key in s_keys:
            if s_dict[key] != t_dict[key]:
                return key