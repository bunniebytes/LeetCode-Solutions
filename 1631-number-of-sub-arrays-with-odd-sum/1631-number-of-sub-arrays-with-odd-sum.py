class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        odd = 0
        even = 0
        _sum = 0

        for num in arr:
            _sum += num
            if _sum % 2 == 0:
                even += 1
                ans += odd
            else:
                odd += 1
                ans += even + 1
        
        return ans % (10**9 + 7)



