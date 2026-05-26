class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {num : idx for idx, num in enumerate(nums)}
        for idx, num in enumerate(nums):
            diff = index_dict.get(target - num)
            if diff and idx != diff:
                return [idx, diff]