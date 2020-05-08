from tictactoe import *


def test_check_valid_coordinate():
    game_ = TTT(" XXOO OX ")
    # print_board(board_)
    fail_test_cases = [
        ["1", "1"],  # occupied
        ["3", "3"],  # occupied
        ["one", "2"],  # should enter number
        ["three", "1"],  # should enter number
        ["0", "1"],  # out of range
        ["2", "4"],  # out of range
    ]
    for case in fail_test_cases:
        assert False == game_.check_valid_coordinate(case)

    success_test_cases = [
        ["1", "3"],
        ["3", "1"],
        ["3", "2"]
    ]
    for case in success_test_cases:
        assert game_.check_valid_coordinate(case)
        print(case, "correct")


def test_row_has_2_symbol():
    game1 = TTT(" XX"
                "OO "
                "OX ")

    game2 = TTT("OXX"
                " OX"
                "OX ")
    game3 = TTT("OXX"
                "OXX"
                " X ")
    test_cases = [
        # X wins cases
        # row
        (game1, [TTT.get_cell(0, 0), TTT.get_cell(0, 1), TTT.get_cell(0, 2)], TTT.X_SYMBOL),
        # column
        (game2, [TTT.get_cell(0, 2), TTT.get_cell(1, 2), TTT.get_cell(2, 2)], TTT.X_SYMBOL),
        # diagonal
        (game3, [TTT.get_cell(0, 2), TTT.get_cell(1, 1), TTT.get_cell(2, 0)], TTT.X_SYMBOL),

        # O wins cases
        # row
        (game1, [TTT.get_cell(1, 0), TTT.get_cell(1, 1), TTT.get_cell(1, 2)], TTT.O_SYMBOL),
        # column
        (game3, [TTT.get_cell(0, 0), TTT.get_cell(1, 0), TTT.get_cell(2, 0)], TTT.O_SYMBOL),
        # diagonal
        (game2, [TTT.get_cell(0, 0), TTT.get_cell(1, 1), TTT.get_cell(2, 2)], TTT.O_SYMBOL),

        # No winner cases
        # row
        (game1, [TTT.get_cell(2, 0), TTT.get_cell(2, 1), TTT.get_cell(2, 2)], TTT.EMPTY_SYMBOL),
        # column
        (game2, [TTT.get_cell(0, 1), TTT.get_cell(1, 1), TTT.get_cell(2, 1)], TTT.EMPTY_SYMBOL),
        # diagonal
        (game3, [TTT.get_cell(0, 0), TTT.get_cell(1, 1), TTT.get_cell(2, 2)], TTT.EMPTY_SYMBOL)
    ]
    for case in test_cases:
        game_ = case[0]
        game_.print_board()
        cell_ = case[1]
        print("Testing ", cell_)
        winner = case[0].row_has_2_symbol(cell_)
        print("Winner is", winner)
        assert case[2] == winner


if __name__ == "__main__":
    # test_check_valid_coordinate()
    test_row_has_2_symbol()
