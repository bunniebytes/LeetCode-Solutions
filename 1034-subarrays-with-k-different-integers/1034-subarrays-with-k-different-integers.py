class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        return self.find_subarray(nums, k) - self.find_subarray(nums, k - 1)

    def find_subarray(self, arr, distinct):
        left = 0
        count = 0
        num_dict = defaultdict(int)

        for right in range(len(arr)):
            if len(num_dict) <= distinct:
                num_dict[arr[right]] += 1

            while len(num_dict) > distinct:
                num_dict[arr[left]] -= 1
                if num_dict[arr[left]] == 0:
                    del num_dict[arr[left]]
                left += 1
            count += right - left + 1

        return count