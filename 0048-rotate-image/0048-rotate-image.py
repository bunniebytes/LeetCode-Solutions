class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row = 0
        len_list = len(matrix)
        max_index = len_list - 1
        while row < len(matrix)/2:
            for col in range(row, max_index - row):
                hold = matrix[row][col]
                prev_row = row
                row = col
                col = max_index - prev_row
                temp = matrix[row][col]
                matrix[row][col] = hold
                hold = temp
                
                prev_row = row
                row = col
                col = max_index - prev_row
                temp = matrix[row][col]
                matrix[row][col] = hold
                hold = temp

                prev_row = row
                row = col
                col = max_index - prev_row
                temp = matrix[row][col]
                matrix[row][col] = hold
                hold = temp

                prev_row = row
                row = col
                col = max_index - prev_row
                
                temp = matrix[row][col]
                matrix[row][col] = hold
                hold = temp
            row += 1

    # def move_inplace(self, row, col, hold):
    #     prev_row = row
    #     row = col
    #     col = max_index - prev_row
    #     temp = matrix[row][col]
    #     matrix[row][col] = hold
    #     hold = temp
    #     return row, col, hold

