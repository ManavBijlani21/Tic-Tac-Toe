#For displaying the board
from IPython.display import clear_output
def display_board(board):
    clear_output()
    print('  ',' |','  ',' |','  ')
    print(board[1],' |',board[2],' |',board[3])
    print('  ',' |','  ',' |','  ')
    print('----------------')
    print('  ',' |','  ',' |','  ')
    print(board[4],' |',board[5],' |',board[6])
    print('  ',' |','  ',' |','  ')
    print('----------------')
    print('  ',' |','  ',' |','  ')
    print(board[7],' |',board[8],' |',board[9])
    print('  ',' |','  ',' |','  ')
    

#Taking choice from the user
def user_choice():
    choice=False
    while choice not in ['X','O']:
        choice=input('Player 1:Do you want to take X or O:')
        if choice not in ['X','O']:
            print("Please enter a valid choice!")
    
    if choice=='X':
        return ('X','O')
    else:
        return ('O','X')

