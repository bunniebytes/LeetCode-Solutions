class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        # find the first average and assign to max_avg
        max_avg = window_sum / k

        # first loop - start at the next index after the window where i = k (because we already found first window)
        for i in range(k, len(nums)):
        # we would add nums[i] to the sum and then subtract nums[i - k] (this slides the window over)
            window_sum += nums[i] - nums[i - k]
            # find the avg of this window if greater than max_avg reassign
            new_avg = window_sum / k
            # print(i, new_avg)

            if new_avg > max_avg:
                max_avg = new_avg

        return max_avg