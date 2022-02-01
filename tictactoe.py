'''
TicTacToe 
Author: Diego A. Gomez
CSE 210
'''


def main ():

    player1, player2 = players()
    player = "x"
   
    game = tictactoe()
   
    while (winner(game)!=False):

        print_tictactoe (game)  
        num = player_move(player)
        player = player_turn(player)
        game [num -1] = player
    print_tictactoe(game)
    print("Good game. Thanks for playing!") 


def players ():
    player1 = input('Enter player 1 name: ')
    player2 = input('Enter player 2 name: ')
    return player1, player2

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
    num = int(input(f"{player}'s turn to choose a square (1-9): "))
    return num

def player_turn (turn):
    if turn == "x":
        return "o"
    elif turn == "o":
        return "x"

def winner (game):
    if (game[0] == game[1] == game[2] or game[3] == game[4] == game[5] or
        game[6] == game[7] == game[8] or game[0] == game[4] == game[8] or
        game[6] == game[4] == game[2] or game[0] == game[3] == game[6] or
        game[1] == game[4] == game[7] or game[2] == game[5] == game[8]):
        return True
    else:
        return False

# def tie (game):




if __name__ == "__main__":
    main()