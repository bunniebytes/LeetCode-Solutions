class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_dict = {0:1}
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            # Python mod will always be positive, but other languages need following if statment if mod is negative.
            # if mod < 0:
            #     mod += k
            if remainder_dict.get(mod):
                ans += remainder_dict[mod]
                remainder_dict[mod] += 1
            else:
                remainder_dict[mod] = 1
        return ans