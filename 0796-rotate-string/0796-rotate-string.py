class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        double_s = s + s
        return goal in double_s and len(goal) == len(s)