from sudokusolver.board import Board

class Game:
    _counter = 0

    def __init__(self, string:str='') -> None:
        self.game_id = Game._counter
        Game._counter += 1
        self.board = Board(string)
        self.iterations = 0

    def sudoku_solve(self):
        if self.board.get_empty_position() is None:
            return True
        else:
            row, col = self.board.get_empty_position()

        for guess in self.board.get_available_values(row,col):
            if self.board.get_is_valid(guess, row, col):
                self.board.set_value(guess,row,col)
                if self.sudoku_solve():
                    return True
            self.board.reset_value(row,col)
        return False

    def get_solution(self):
        return self.board.print_grid()
