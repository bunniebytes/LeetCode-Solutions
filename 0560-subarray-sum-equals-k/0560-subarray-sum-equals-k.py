class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        hash_map = {0:1}
        _sum = 0
        for num in nums:
            _sum += num
            mod = _sum - k
            if hash_map.get(mod):
                ans += hash_map[mod]
            if hash_map.get(_sum):
                hash_map[_sum] += 1
            else:
                hash_map[_sum] = 1
            
        return ans