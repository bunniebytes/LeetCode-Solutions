class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        for idx, x in enumerate(nums):
            if x == 0:
                zeroes += 1
            else:
                nums[idx] = 0
                nums[idx - zeroes] = x