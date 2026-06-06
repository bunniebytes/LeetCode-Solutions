class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        left_sums = [0] * len_nums
        right_sums = [0] * len_nums
        results = [0] * len_nums
        left_prev = right_prev = 0
        max_index = len_nums - 1

        for _idx in range(max_index):
            right_idx = max_index - _idx
            left_sums[_idx] = left_prev
            left_prev += nums[_idx]
            right_sums[right_idx] = right_prev
            right_prev += nums[right_idx]
            if _idx == max_index - 1:
                left_sums[_idx + 1] = left_prev
                right_sums[right_idx - 1] = right_prev

        for _idx in range(len_nums):
            results[_idx] = abs(left_sums[_idx] - right_sums[_idx])
            
        return results
