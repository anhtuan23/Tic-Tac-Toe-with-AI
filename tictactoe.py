import players
from board import Board


class Game:
    is_player1_turn = True
    DEBUG = False

    def __init__(self, board_, player1_, player2_):
        self.board = board_
        self.player1 = player1_
        self.player2 = player2_

    def play(self):
        while True:
            if Game.is_player1_turn:
                cell = player1.get_next_move(self.board)
            else:
                cell = player2.get_next_move(self.board)

            is_game_over = self.board.insert_move(cell)
            self.board.print_board()
            if is_game_over:
                self.board.print_game_state()
                break

            Game.is_player1_turn = not Game.is_player1_turn


def is_command_valid(command_, player_types_):
    if command == "exit":
        return True

    params_ = command_.split()
    if len(params_) == 3 and params_[0] == "start" and params_[1] in player_types_ and params_[2] in player_types_:
        return True

    print("Bad parameters!")
    return False


###############################################
if __name__ == "__main__":
    # Initial command loop
    while True:
        command = input("Input command: ")
        # command = "start hard hard"
        if is_command_valid(command, players.player_types):
            break

    # Main program loop
    if command != "exit":
        _, player1_type, player2_type = command.split()

        player1 = players.player_factory(player1_type)
        player2 = players.player_factory(player2_type)

        game = Game(Board(), player1, player2)
        game.play()
