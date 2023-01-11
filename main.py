from sudokusolver import game

if __name__ == "__main__":
    puzzle = input("Paste sudoku as a string of digits: ")
    game = game.Game(puzzle)
    print(game.get_solution())
    if game.sudoku_solve():
        print(game.get_solution())
