import itertools
import random


class Board:
    X_SYMBOL = "X"
    O_SYMBOL = "O"
    PLAYER_SYMBOLS = X_SYMBOL, O_SYMBOL
    EMPTY_SYMBOL = " "

    EMPTY_BOARD = "         "

    def __init__(self, board_string=EMPTY_BOARD):
        self.board = self.get_board(board_string)

    @staticmethod
    def get_board(board_string_, board_length=3):
        board_ = []
        count = 0
        while count < len(board_string_):
            board_.append([board_string_[i] for i in range(count, count + board_length)])
            count += board_length
        return board_

    @staticmethod
    def get_cell(row_id, column_id):
        return {"row": row_id, "column": column_id}

    @staticmethod
    def get_move(cell_, symbol_):
        return {"cell": cell_, "symbol": symbol_}

    def get_cell_content(self, cell_):
        return self.board[cell_.get("row")][cell_.get("column")]

    def print_board(self, tab=""):
        print(tab, "---------")
        for row in self.board:
            print(tab, "|", " ".join(row), "|")
        print(tab, "---------")

    def is_all_cell_equal(self, cells):
        if len(cells) == 0:
            return True
        first_cell = self.get_cell_content(cells[0])
        # Check all cell content equals to first cell content
        for cell_ in cells:
            if first_cell != self.get_cell_content(cell_):
                return False
        return True

    def row_has_2_symbol(self, row):
        row_content = [self.get_cell_content(cell_) for cell_ in row]
        for symbol in Board.PLAYER_SYMBOLS:
            if row_content.count(symbol) == 2 and row_content.count(Board.EMPTY_SYMBOL) == 1:
                return symbol
        return Board.EMPTY_SYMBOL

    def get_first_empty_cell_in_row(self, row_):
        """Get the first empty cell in a row"""
        for cell_ in row_:
            if self.get_cell_content(cell_) == Board.EMPTY_SYMBOL:
                return cell_

    @staticmethod
    def input_coordinate_to_cell(column, row, board_length):
        m_col_ = column - 1
        m_row_ = board_length - row
        return Board.get_cell(m_row_, m_col_)

    def check_valid_coordinate(self, coordinate_):
        try:
            column = int(coordinate_[0])
            row = int(coordinate_[1])
        except IndexError:
            print("Not enough coordinate!")
            return False
        except ValueError:
            print("You should enter numbers!")
            return False

        board_length = len(self.board)
        if column > board_length or row > board_length \
                or column < 1 or row < 1:
            print(f"Coordinates should be from 1 to {board_length}!")
            return False

        cell_ = self.input_coordinate_to_cell(column, row, board_length)
        if self.get_cell_content(cell_) != Board.EMPTY_SYMBOL:
            print("This cell is occupied! Choose another one!")
            return False

        return True

    def get_move_from_coordinate(self, coordinate_):
        column_ = int(coordinate_[0])
        row_ = int(coordinate_[1])
        cell_ = Board.input_coordinate_to_cell(column_, row_, len(self.board))
        symbol_ = self.get_next_move_symbol()
        return Board.get_move(cell_, symbol_)

    def insert_move(self, move_):
        cell_ = move_["cell"]
        symbol_ = move_["symbol"]

        column_ = cell_["column"]
        row_ = cell_["row"]
        self.board[row_][column_] = symbol_

        return self.is_game_over()

    def get_next_move_symbol(self):
        x_number = 0
        o_number = 0
        for c in itertools.chain(*self.board):
            if c == Board.X_SYMBOL:
                x_number += 1
            elif c == Board.O_SYMBOL:
                o_number += 1
        next_move_symbol = Board.X_SYMBOL if x_number == o_number else Board.O_SYMBOL
        return next_move_symbol

    def get_opponent_move_symbol(self, current_symbol):
        for symbol in Board.PLAYER_SYMBOLS:
            if symbol != current_symbol:
                return symbol

    def get_random_move(self):
        empty_cells = self.get_empty_cells()
        chosen_cell = random.choice(empty_cells)
        symbol_ = self.get_next_move_symbol()
        return Board.get_move(chosen_cell, symbol_)

    def get_win_moves(self):
        all_three_in_row = self.get_all_three_in_rows()
        winning_moves = []
        for row in all_three_in_row:
            winner = self.row_has_2_symbol(row)
            if winner != Board.EMPTY_SYMBOL:
                empty_cell = self.get_first_empty_cell_in_row(row)
                winning_moves.append(Board.get_move(empty_cell, winner))
        return winning_moves

    def get_symbol_win_moves(self, symbol_):
        all_winning_moves = self.get_win_moves()
        return [move for move in all_winning_moves if move["symbol"] == symbol_]

    def get_empty_cells(self):
        cells = [Board.get_cell(row, column) for row in range(len(self.board)) for column in range(len(self.board))]
        return [cell_ for cell_ in cells if self.get_cell_content(cell_) == Board.EMPTY_SYMBOL]

    def has_empty_cell(self):
        return len(self.get_empty_cells()) > 0

    def get_row(self, row_):
        row = []
        for column in range(len(self.board)):
            row.append(Board.get_cell(row_, column))
        return row

    def get_column(self, column_):
        column = []
        for row in range(len(self.board)):
            column.append(Board.get_cell(row, column_))
        return column

    def get_diagonal(self, forward=False):
        if forward:
            return [Board.get_cell(0, 2), Board.get_cell(1, 1), Board.get_cell(2, 0)]
        else:  # backward diagonal
            return [Board.get_cell(0, 0), Board.get_cell(1, 1), Board.get_cell(2, 2)]

    def get_all_three_in_rows(self):
        three_in_rows = [self.get_diagonal(forward=True), self.get_diagonal(forward=False)]
        for i in range(3):
            three_in_rows.append(self.get_row(i))
            three_in_rows.append(self.get_column(i))
        return three_in_rows

    def check_winner(self):
        """Return the winning symbol TicTacToe.X_SYMBOL or TicTacToe.O_SYMBOL
        returns TicTacToe.EMPTY_SYMBOL if there is no winner
        """
        # Get all possible 3 in rows
        for three in self.get_all_three_in_rows():
            if self.is_all_cell_equal(three) and self.get_cell_content(three[0]) != Board.EMPTY_SYMBOL:
                return self.get_cell_content(three[0])

        return Board.EMPTY_SYMBOL

    def is_game_over(self):
        return self.check_winner() != Board.EMPTY_SYMBOL or not self.has_empty_cell()

    def print_game_state(self):
        winner = self.check_winner()
        if winner == Board.EMPTY_SYMBOL:
            print("Draw")
        else:
            print(f"{winner} wins")
        return
