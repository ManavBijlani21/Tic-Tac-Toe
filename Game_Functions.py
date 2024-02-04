#For displaying the board
from IPython.display import clear_output
import random

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

#Checking the win condition
def win_check(board,mark):
    win=False
    #Conditions to check every possible winnning condition
    if (board[1]==board[2]==board[3]==' '+mark) or (board[4]==board[5]==board[6]==' '+mark) or (board[7]==board[8]==board[9]==' '+mark):
        win=True
    elif (board[1]==board[4]==board[7]==' '+mark) or (board[2]==board[5]==board[8]==' '+mark) or (board[3]==board[6]==board[9]==' '+mark):
        win=True
    elif (board[1]==board[5]==board[9]==' '+mark) or (board[3]==board[5]==board[7]==' '+mark):
        win=True
    else:
        pass
    
    return win 

#Checking which user goes first
def first_move():
    lst=['Player 1','Player 2']
    #Using the randint function of the random library to make a random choice
    rand=random.randint(0,1)
    return lst[rand]


#To check if the given position is empty
def space_check(board,position):
    if board[position]=='  ':
        return True
    else:
        return False


#To check whether the board is full or not
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


#Taking the position where marker needs to be placed
def position_choice(board):
    marker=0
    while marker not in [i for i in range(1,10)] or not(space_check(board,marker)):
        marker=int(input("Choose a position where you want to place your mark(1-9):"))

        #Checking if the given input is valid
        if marker not in [i for i in range(1,10)]:
            print("Please enter your marker in the given range!")
            continue
        if not(space_check(board,marker)):
            print("Please enter a position which is not yet filled..")
    return marker


#Placing the marker on the board
def place_marker(board,position,mark):
    board[position]=' '+mark


#Asking for a replay from the user
def replay():
    to_continue=False
    while to_continue not in ['Y','N']:
        to_continue=input("Do you want to play more(Y/N)?")
        if to_continue not in ['Y','N']:
            print("Please enter a valid choice!")
    
    if to_continue=='Y':
        return True
    else:
        return False
    

