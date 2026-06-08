class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        before = []
        _pivot = []
        after = []
        for num in nums:
            if num < pivot:
                before.append(num)
            elif num > pivot:
                after.append(num)
            else:
                _pivot.append(num)

        return before + _pivot + after
        