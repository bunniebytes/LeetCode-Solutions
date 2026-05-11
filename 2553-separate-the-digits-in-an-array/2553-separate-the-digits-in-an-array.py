class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        results = []
        for num in nums:
            results += map(int, list(str(num)))
            # results += [int(n) for n in str(num)]

        return results