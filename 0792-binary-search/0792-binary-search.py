class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        # loop while low is less or equal to high
        while low <= high:
            # recalculate mid with new low and high
            mid = (low + high) // 2
            # if target is nums[mid] return mid
            if target == nums[mid]:
                return mid
            # if target if greater than nums[mid] reassign low
            if target > nums[mid]:
                low = mid + 1
            # if target is less than nums[mid] reassign high
            if target < nums[mid]:
                high = mid - 1
        return -1
            # once low is greater than high we stop
        