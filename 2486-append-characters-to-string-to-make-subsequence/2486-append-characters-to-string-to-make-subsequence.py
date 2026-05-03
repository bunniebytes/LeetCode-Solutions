class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_idx = 0
        t_idx = 0
        while s_idx < len(s) and t_idx < len(t):
            # check if letter at s_idx and t_idx are the same
            if s[s_idx] == t[t_idx]:
                s_idx += 1
                t_idx += 1
            else:
                s_idx += 1

        return len(t) - t_idx