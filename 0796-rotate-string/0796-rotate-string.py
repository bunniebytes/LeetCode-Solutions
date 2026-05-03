class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        goal_dict = defaultdict(list)
        first_letter = s[0]
        # check len(s) and len(g) are same
        if len(s) != len(goal):
            return False
        if len(s) == 1:
            return s == goal
        # loop through and get dictionary of goals letters and indexes
        for x in range(len(s)):
            goal_dict[goal[x]].append(x)
        # get first letter of s and look up in dictionary and get list of indexes
        first_letter_indices = goal_dict.get(first_letter)
        # loop through and slice/Frankenstein goal and check if they equal
        if first_letter_indices:
            for idx in first_letter_indices:
                frankenstein = goal[idx:] + goal[:idx]
                if s == frankenstein:
                    return True
        return False