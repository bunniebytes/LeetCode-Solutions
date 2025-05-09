class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_nums = len(nums)
        if len_nums > 0:
            last_idx = len_nums - 1
        if val not in nums:
            return len_nums

        for x in range(len_nums):
            if nums[x] == val:
                while x < last_idx:
                    if nums[last_idx] == val:
                        last_idx -= 1
                    else:
                        break
                nums[x] = nums[last_idx]
                nums[last_idx] = val
            if x == last_idx:
                return x