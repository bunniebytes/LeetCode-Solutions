class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        result = []
        # loop through and add count each time I see a number
        for num in nums:
            counts[num] += 1

        # sort values and slice to k
        values_sorted = set(sorted(counts.values(), reverse = True)[:k])

        # loop through k, v in dictionary and if in list add to result
        for key, val in counts.items():
            if val in values_sorted:
                result.append(key)

        return result

        