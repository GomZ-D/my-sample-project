'''
TicTacToe 
Author: Diego A. Gomez
CSE 210
'''
import os

def main ():

    # player1, player2 = players()
    player = ""
    count = 0
    
    game = tictactoe()
   
   
    while not (winner(game)==True or count == 9): 
        os.system('cls')
        player = player_turn(player)
        print_tictactoe (game)
        num = player_move(player)
        game [num -1] = player
        count = count + 1
        outcome = winner(game)
        champ = player
    
    
    print_tictactoe(game)
    tie(count,outcome,champ)    
    print("Good game. Thanks for playing!")

# def players ():
#     player1 = input('Enter player 1 name: ')
#     player2 = input('Enter player 2 name: ')
#     return player1, player2

# def players (player):
#     if player.upper() == "X":
#         print('Player X is the Champion! Game Over')
#     elif player.upper() == "O":
#         print('Player O is the Champion! Game over')
        
def tictactoe():
    game=[]
    for num in range (9):
        game.append(num + 1)
    return game



def print_tictactoe(game):
    print("\n")
    
    print("\t {} | {} | {}".format(game[0], game[1], game[2]))
    print('\t___|___|___')
    
 
    print("\t   |   |")
    print("\t {} | {} | {}".format(game[3], game[4], game[5]))
    print('\t___|___|___')
 
     
    print("\t   |   |")
    print("\t {} | {} | {}".format(game[6], game[7], game[8]))
    print("\n")


def player_move (player):
    validation = False
    while validation == False:
        num = input(f"{player}'s turn to choose a square (1-9): ")
        if num == "1" or num == "2" or num == '3' or num == '4' or num == '5' or num == '6' or num == '7' or num == '8' or num== '9':
            validation = True
        else:
            validation = False
    num2 = int(num)
    return num2


def player_turn (turn):
    if turn == "" or turn.upper() == "O":
        return "X"
    elif turn.upper() == "X":
        return "O"


def winner (game):
    if (game[0] == game[1] == game[2] or game[3] == game[4] == game[5] or
        game[6] == game[7] == game[8] or game[0] == game[4] == game[8] or
        game[6] == game[4] == game[2] or game[0] == game[3] == game[6] or
        game[1] == game[4] == game[7] or game[2] == game[5] == game[8]):
        return True
    else:
        return False

def tie (count,outcome,champ):
    if count >= 9 and outcome == False:
        print("It's a Tie!!")
    elif outcome == True:
        print(f"{champ} is the champion! ")

    
# def scoreboard (points, player):
#     print("\t--------------------------------")
#     print("\t              SCOREBOARD       ")
#     print("\t--------------------------------")



if __name__ == "__main__":
    main()