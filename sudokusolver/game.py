from sudokusolver.board import Board

class Game:
    _counter = 0

    def __init__(self, string:str) -> None:
        self.game_id = Game._counter
        Game._counter += 1
        self.board = Board(string)
        self.iterations = 0

    def sudoku_solve(self):
        solved = False
        while solved == False:
            self.iterations += 1
            for row in range(self.board.get_grid().shape[0]):
                for col in range(self.board.get_grid().shape[1]):
                    if self.board.is_zero(row,col):
                        available_values = self.board.available_values(row,col)
                        if len(available_values) == 1 and self.board.get_is_possible(available_values[0], row, col):
                            self.board.set_value(available_values[0],row,col)
            solved = self.board.get_is_valid()

    def get_solution(self):
        return self.board.get_grid()
