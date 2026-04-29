class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        number_houses = len(colors)
        last_index = right_index = len(colors) - 1
        first_color = last_color = None
        for left_index in range(number_houses):
            if first_color is None and last_color is None:
                first_color = colors[left_index]
                last_color = colors[last_index]
                if first_color != last_color:
                    return last_index
                right_index -= 1
                continue
            if first_color != colors[right_index]:
                return abs(0 - right_index)
            if last_color != colors[left_index]:
                return abs(left_index - last_index)
            right_index -= 1