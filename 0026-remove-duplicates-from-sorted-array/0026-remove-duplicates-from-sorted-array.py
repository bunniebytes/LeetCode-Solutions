class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        idx = 0
        k = len(set(nums))
        for x in nums:
            if prev is None:
                prev = x
                idx += 1
            elif prev != x:
                nums[idx] = x
                prev = x
                idx += 1


        print(nums)
        return k