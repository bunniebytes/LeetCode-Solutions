class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # find length of all lists in list using map and then set()
        wall_height = len(wall)
        len_lists = set(map(len, wall))
        width_count = defaultdict(int)
        # if len(set) is 1 and 1 in set - return len(lists)
        if len(len_lists) == 1 and 1 in len_lists:
            return wall_height
        # loop through lists of lists
        for row in wall:
            _sum = 0
        #     loop through list
            for brick in row[:-1]:
                _sum += brick
                width_count[_sum] += 1

        # find max in values
        max_edges = max(list(width_count.values()))
        return wall_height - max_edges