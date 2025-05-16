class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        len_nums = len(nums)
        for idx, num in enumerate(nums):
            if target == num or target < num:
                return idx
            elif idx == len_nums - 1:
                return len_nums