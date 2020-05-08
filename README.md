
# Tic-Tac-Toe-with-AI
Implementation of Hyperskill project with the same name: https://hyperskill.org/projects/82

To run:

    python tictactoe.py

Next, the `Input command: >` prompt should appear.

The command has the following format:

    start player1_type player2_type
There are 4 player types:
|Type|Description  |
|--|--|
| `user` | human player |
| `easy` | AI player, placing moves at random |
| `medium` | AI player, going one move ahead to see an immediate win or prevent an immediate loss |
| `hard` | AI player, using Minimax algorithm, can see all possible outcomes till the end of the game and choose the best of them considering his opponent also would play perfectly|

The example below shows how your program should work.
The greater-than symbol followed by space (> ) represents the user input. Notice that it's not the part of the input.

    Input command: > start hard user  
    Making move level "hard"  
    ---------  
    |       |  
    | X     |  
    |       |  
    ---------  
    Enter the coordinates: > 2 2  
    ---------  
    |       |  
    | X O   |  
    |       |  
    ---------  
    Making move level "hard"  
    ---------  
    | X     |  
    | X O   |  
    |       |  
    ---------  
    Enter the coordinates: > 2 1  
    ---------  
    | X     |  
    | X O   |  
    | O     |  
    ---------  
    Making move level "hard"  
    ---------  
    | X X   |  
    | X O   |  
    | O     |  
    ---------  
    Enter the coordinates: > 1 1  
    ---------  
    | X X   |  
    | X O   |  
    | O O   |  
    ---------  
    Making move level "hard"  
    ---------  
    | X X X |  
    | X O   |  
    | O O   |  
    ---------  
    X wins  
      
    Input command: > exit
