import copy

import tictactoe
from board import Board

USER_TYPE = "user"
EASY_TYPE = "easy"
MEDIUM_TYPE = "medium"
HARD_TYPE = "hard"
player_types = USER_TYPE, EASY_TYPE, MEDIUM_TYPE, HARD_TYPE


def player_factory(player_type):
    if player_type == USER_TYPE:
        return User()
    elif player_type == EASY_TYPE:
        return EasyAi()
    elif player_type == MEDIUM_TYPE:
        return MediumAi()
    elif player_type == HARD_TYPE:
        return HardAi()


class User:
    def get_next_move(self, board_):
        while True:
            coordinate_ = input("Enter the coordinates: ").split()
            # coordinate = "3 1".split()
            if board_.check_valid_coordinate(coordinate_):
                return board_.get_move_from_coordinate(coordinate_)


class EasyAi:
    def get_next_move(self, board_):
        print(f'Making move level "{EASY_TYPE}"')
        return board_.get_random_move()


class MediumAi:
    def get_next_move(self, board_):
        print(f'Making move level "{MEDIUM_TYPE}"')

        current_symbol = board_.get_next_move_symbol()
        opponent_symbol = board_.get_opponent_move_symbol(current_symbol)

        winning_moves = board_.get_win_moves()

        # 1. If it can win in one move (if it has two in a row),
        # it places a third to get three in a row and win.
        for move in winning_moves:
            symbol = move["symbol"]
            if symbol == current_symbol:
                return move

        # 2. If the opponent can win in one move,
        # it plays the third itself to block the opponent to win.
        for move in winning_moves:
            symbol = move["symbol"]
            if symbol == opponent_symbol:
                move["symbol"] = current_symbol
                return move

        # 3. Otherwise, it makes a random move
        return board_.get_random_move()


class HardAi:
    def get_next_move(self, board_):
        print(f'Making move level "{HARD_TYPE}"')

        # For the first move, just choose by random
        if len(board_.get_empty_cells()) == 9:
            return board_.get_random_move()

        symbol = board_.get_next_move_symbol()
        best_route = HardAi.minimax(board_, symbol, 0)
        return Board.get_move(best_route["cell"], symbol)

    @staticmethod
    def get_route(score_, cell_):
        return {"score": score_, "cell": cell_}

    @staticmethod
    def minimax(board_, player_symbol_, stage):
        current_symbol = board_.get_next_move_symbol()

        # STOP CONDITION: if the game can be won in one more move:
        winning_moves = board_.get_symbol_win_moves(current_symbol)
        if len(winning_moves) > 0:
            score = 10 if current_symbol == player_symbol_ else -10
            route = HardAi.get_route(score, winning_moves[0]["cell"])
            HardAi.print_debug(board_, route, stage, terminal_score=score)
            # returns cell too in case the evaluation only has 1 stage
            return route
        # If the board is full, the game is draw
        if not board_.has_empty_cell():
            route = HardAi.get_route(0, None)
            HardAi.print_debug(board_, route, stage, terminal_score=0)
            return route

        # RECURSION
        empty_cells = board_.get_empty_cells()
        next_symbol = board_.get_next_move_symbol()
        routes = list()
        for cell in empty_cells:
            new_board = copy.deepcopy(board_)
            new_board.insert_move(Board.get_move(cell, next_symbol))
            route = HardAi.minimax(new_board, player_symbol_, stage + 1)
            route["cell"] = cell
            routes.append(route)
            HardAi.print_debug(new_board, route, stage)

        max_route = routes[0]
        for route in routes:
            if route["score"] > max_route["score"]:
                max_route = route

        min_route = routes[0]
        for route in routes:
            if route["score"] < min_route["score"]:
                min_route = route

        return max_route if next_symbol == player_symbol_ else min_route

    @staticmethod
    def print_debug(board_, route, stage, terminal_score=None):
        tab = "    " * stage  # for debug printing
        if tictactoe.Game.DEBUG:
            print(tab, "[[[", stage)
            board_.print_board(tab)
            if terminal_score != None:
                print(tab, "TERMINAL: ", terminal_score)
            print(tab, "Score:", route["score"])
            print(tab, "]]]")
