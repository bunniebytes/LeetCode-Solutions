class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        for x in range(nums_len):
            y = x + 1
            if nums[x] == 0 and x != nums_len - 1:
                # check if next num is not 0
                while y < nums_len - 1:
                    if nums[y] == 0:
                        y += 1
                    else:
                        break
                nums[x] = nums[y]
                nums[y] = 0
                        