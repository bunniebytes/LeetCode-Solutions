class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # stones = 0
        rotate_dict = defaultdict(list)

        # loop through row list
        for col_idx, row in enumerate(boxGrid):
            stones = 0
            for row_idx, cell in enumerate(row):
                rotate_dict[row_idx].insert(0, cell)
                if cell == "#":
                    stones += 1
                elif cell == "." and stones > 0:
                    rotate_dict[row_idx][0] = "#"
                    print(stones)
                    print(row_idx - stones)
                    rotate_dict[row_idx - stones][0] = "."
                else:
                    stones = 0

        return list(rotate_dict.values())
