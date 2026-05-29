class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_sum = float("inf")

        for num in nums:
            curr_sum = 0
            while num > 9:
                curr_sum += num % 10
                num //= 10
            curr_sum += num #this adds the last number
            if curr_sum < min_sum:
                min_sum = curr_sum
        return min_sum
