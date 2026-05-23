class Solution:
    def check(self, nums: List[int]) -> bool:
        decrease = 0
        split = None
        for idx in range(len(nums) - 1):
            if nums[idx] > nums[idx + 1]:
                decrease += 1
                split = idx
            if (split is not None and nums[0] < nums[-1]) or decrease > 1:
                    return False
        return True