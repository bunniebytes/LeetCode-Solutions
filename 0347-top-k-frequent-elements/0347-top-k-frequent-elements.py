class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        counts_array = [[] for _ in range(len(nums) + 1)]
        result = []
        # loop through and add count each time I see a number
        for num in nums:
            counts[num] += 1
        # loop through key and input and append to list at index
        for num, count in counts.items():
            counts_array[count].append(num)

        # iterate over the list of lists(called item) in reverse
        for item in counts_array[::-1]:
            result += item
            if len(result) == k:
                return result