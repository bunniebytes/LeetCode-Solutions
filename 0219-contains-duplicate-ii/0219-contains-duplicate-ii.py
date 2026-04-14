class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        # loop through the range(len) (so we only have to loop through once)
        for i in range(len(nums)):
            if nums[i] in seen: # (we know window is <= k)
                return True

            # if nums[i] is not in seen add to seen
            seen.add(nums[i])

            # if the window is bigger than k we need to remove the value at the smallest index in the window - which is the current index (i) we are at minus k
            if len(seen) > k:
                smallest_index = i - k
                seen.remove(nums[smallest_index])

        return False