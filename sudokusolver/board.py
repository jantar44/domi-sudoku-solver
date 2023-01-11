import numpy as np

class Board:
    def __init__(self, string):
        self.grid = self.string_to_line(string)

    @staticmethod
    def string_to_line(string):
        try:
            return np.array([string]).view('<U1').astype(int).reshape(9, 9)
        except ValueError:
            print('Initial board is wrong length.')
    @staticmethod
    def get_inner_grid(grid, row, col):
        inner_row = row//3*3
        inner_col = col//3*3
        return grid[inner_row:inner_row+3, inner_col:inner_col+3]

    def get_is_valid(self, value, row, col):
        valid = True
        #row
        for i in range(len(self.grid[0])):
            if self.get_value(row,i) == value:
                valid = False
        #col
        for j in range(len(self.grid)):
            if self.get_value(j, col) == value:
                valid = False
        #inner grid
        if value in self.get_inner_grid(self.grid, row, col):
            valid = False

        return valid

    def get_empty_position(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.get_value(i, j) == 0:
                    return i, j
        return None

    def get_available_values(self, row, col):
        candidates = [i for i in range(1,10)]
        existing_row_values = list(set(self.grid[row,:]))
        existing_col_values = list(set(self.grid[:,col]))
        existing_inn_values = list(set([item for subl in self.get_inner_grid(self.grid, row, col) for item in subl]))
        existing_values = list(set(existing_row_values + existing_col_values + existing_inn_values))
        available_values = [i for i in candidates if i not in existing_values]
        return available_values

    def set_value(self, value, row, col):
        self.grid[row, col]  = value

    def get_value(self, row, col):
        return self.grid[row, col]

    def print_grid(self):
        return np.matrix(self.grid)

