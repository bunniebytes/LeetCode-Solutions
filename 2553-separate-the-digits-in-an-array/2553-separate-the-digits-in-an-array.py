class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        results = []
        for num in nums:
            temp = []
            while num >= 10:
                r = num % 10
                num = num // 10
                temp.append(r)
            results.append(num)
            results += reversed(temp)
        return results