class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        # stones = 0
        num_col = len(boxGrid)
        num_row = len(boxGrid[0])
        rotated_list = [[] for x in range(num_row)]

        # loop through row list
        for col_idx, row in enumerate(boxGrid):
            stones = 0
            for row_idx, cell in enumerate(row):
                rotated_list[row_idx].insert(0, cell)
                if cell == "#":
                    stones += 1
                elif cell == "." and stones > 0:
                    rotated_list[row_idx][0] = "#"
                    rotated_list[row_idx - stones][0] = "."
                else:
                    stones = 0

        return rotated_list
