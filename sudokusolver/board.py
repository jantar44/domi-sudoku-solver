import numpy as np

class Board:
    def __init__(self, string):
        self.grid = self.string_to_line(string)

    def get_grid(self):
        return self.grid

    @staticmethod
    def string_to_line(string):
        try:
            return np.array([string]).view('<U1').astype(int).reshape(9, 9)
        except ValueError:
            print('Initial board is wrong length.')

    def inner_grid(self, grid, inner_row, inner_col):
        return grid[inner_row:inner_row+3,inner_col:inner_col+3]

    def get_is_possible(self, value, row, col):
        temp_grid = self.get_grid()
        temp_grid[row, col] = value
        inner_row = np.floor(row/3).astype(int)*3
        inner_col = np.floor(col/3).astype(int)*3
        valid = True
        valid = valid and np.all(np.diff(np.sort(temp_grid, axis=1), axis=1) == 1)
        valid = valid and np.all(np.diff(np.sort(temp_grid, axis=0), axis=0) == 1)
        valid = valid and len(np.unique(self.inner_grid(temp_grid, inner_row, inner_col))) == \
            self.inner_grid(temp_grid, inner_row, inner_col).size
        return valid

    def is_zero(self, row, col):
        if self.get_value(row, col) == 0:
            return True
        else:
            return False

    def available_values(self, row, col):
        candidates = [i for i in range(1,10)]
        temp_grid = self.get_grid()
        inner_row = np.floor(row/3).astype(int)*3
        inner_col = np.floor(col/3).astype(int)*3
        existing_row_values = list(set(temp_grid[row,:]))
        existing_col_values = list(set(temp_grid[:,col]))
        existing_inn_values = list(set([item for subl in temp_grid[inner_row:inner_row+3,inner_col:inner_col+3] for item in subl]))
        existing_values = list(set(existing_row_values + existing_col_values + existing_inn_values))
        available_values = [i for i in candidates if i not in existing_values]
        return available_values

    def set_value(self, value, row, col):
        self.grid[row, col]  = value

    def get_value(self, row, col):
        return self.grid[row, col]

    def get_is_valid(self):
        valid = True
        valid = valid and np.all(np.diff(np.sort(self.grid, axis=1), axis=1) == 1)  # row
        valid = valid and np.all(np.diff(np.sort(self.grid, axis=0), axis=0) == 1)  # column
        for row in range (0,self.grid.shape[0],3):
            for col in range (0,self.grid.shape[1],3):
                valid = valid and len(np.unique(self.grid[row:row+3,col:col+3])) == self.grid[row:row+3,col:col+3].size
        if np.any(self.grid == 0):
            valid = False
        return valid

# i = Board('100039200000402000072000006760005043090010600000700009010293004007000008300860021')
# print(i.grid)
# print('result ',i.available_values(0,1))

