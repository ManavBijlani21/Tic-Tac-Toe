import Game 
from IPython.display import clear_output
import random

#This segment of the code implements the game logic by integrating all the declared functions and printing the desired output
print('Welcome to Tic Tac Toe!')
to_continue=True

while to_continue:
    #Declaring an empty board
    board=['  ']*10
    Game.display_board(board)
    player1_mark,player2_mark=Game.user_choice()
    move=Game.first_move()
    print(move+' goes first')
    game_on=True
    while game_on:
        if move=='Player 1':
            print('Turn of Player 1')
            position=Game.position_choice(board)
            Game.place_marker(board,position,player1_mark)
            Game.display_board(board)
            #Checking if Player 1 wins the game
            if Game.win_check(board,player1_mark):
                print('Congratulations!!!Player 1 has won')
                game_on=False
            else:
                if Game.full_board_check(board):
                    print("The game is tied!")
                    game_on=False
                #If none of the above condition satisfied, set the move to Player 2
                else:
                    move='Player 2'
        else:
            print('Turn of Player 2')
            position=Game.position_choice(board)
            Game.place_marker(board,position,player2_mark)
            Game.display_board(board)
            if Game.win_check(board,player2_mark):
                print('Congratulations!!!Player 2 has won')
                game_on=False
            else:
                #If the board is full and no one wins, print that the game is tied
                if Game.full_board_check(board):
                    print("The game is tied!")
                    game_on=False
                else:
                    move='Player 1'
    #Option for game replay
    to_continue=Game.replay()


print('Hope you enjoyed the game!')
print('Thanks for coming :-)')
