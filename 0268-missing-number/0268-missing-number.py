class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Approach 2: O(n lg n) + O(n) ===> O(n lg n)
        # sort input: O(n lg n)
        nums.sort()

        #is everything in its place? O(n)
        #e.g. zeroth element is 0
        # 1st element is 1, etc
        for idx, num in enumerate(nums):
            if idx != num:
                return idx
        return len(nums)

