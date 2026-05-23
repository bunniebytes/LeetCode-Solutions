class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        # double_nums = nums * 2
        first_item = sorted_nums[0]
        slice_idx = []
        for idx, num in enumerate(nums):
            if first_item == num:
                slice_idx.append(idx)
        for idx in slice_idx:
            sliced_nums = nums[idx:]+nums[:idx]
            if sorted_nums == sliced_nums:
                return True
        return False