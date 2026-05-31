class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        first, last = intervals[0]
        output = []

        for idx in range(1, len(intervals)):
            temp_first, temp_last = intervals[idx]
            if last >= temp_first and last < temp_last:
                last = temp_last
            if last < temp_first:
                output.append([first, last])
                if idx < len(intervals):
                    first, last = temp_first, temp_last
        output.append([first, last])

        return output