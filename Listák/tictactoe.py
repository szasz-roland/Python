import random

board = ["1","2","3",
         "4","5","6",
         "7","8","9"]

def game_Board():
    print("|---+---+---|")
    print("|",board[0],   "|" , board[1] , "|" , board[2] , "|" )
    print("|---+---+---|")
    print("|",board[3],   "|" , board[4] , "|" ,board[5] , "|" )
    print("|---+---+---|")
    print("|",board[6],   "|" , board[7] , "|" , board[8] , "|" )
    print("|---+---+---|")


    
    
print("Válassz: X vagy O ")
player = str(input())
computer = ""

def player_func():
    global player

    if player == "X":
        computer = "O"
        print("A számítógép " , computer)
    if player == "x":
        player = "X"
        computer = "O"
        print("A számítógép " , computer)
    elif player == "O":
        computer = "X"
        print("A számítógép " , computer)
    elif player == "o":
        player = "o"
        computer = "X"
        print("A számítógép " , computer)

    elif player != "O" or player != "X" or player != "x" or player != "o":
        print("Ezt nem válsaszthatod! Válassz újra!>")
        
player_func()

def game():
    game_Board()

game()


pc_moves = [1,2,3,4,5,6,7,8,9]
pc_move = random.choice(pc_moves)
 
game_proba = 0
while game_proba != 9:
    player_move = int(input("Add meg a lehejezendő formád helyét > "))

    game_Board()

    if board[1] == board[2] == board[3] == player:
        print("Nyertél!")
    elif board[4] == board[5] == board[6] == player:
        print("Nyertél!")
    elif board[7] == board[8] == board[9] == player:
        print("Nyertél!")
    elif board[1] == board[4] == board[7] == player:
        print("Nyertél!")
    elif board[2] == board[5] == board[8] == player:
        print("Nyertél!")
    elif board[3] == board[6] == board[9] == player:
        print("Nyertél!")
    elif board[1] == board[5] == board[9] == player:
        print("Nyertél!")
    elif board[3] == board[5] == board[7] == player:
        print("Nyertél!")
    elif board[1] == board[2] == board[3] == computer:
        print("A számítógép nyert!")
    elif board[4] == board[5] == board[6] == computer:
        print("A számítógép nyert!")
    elif board[7] == board[8] == board[9] == computer:
        print("A számítógép nyert!")
    elif board[1] == board[4] == board[7] == computer:
        print("A számítógép nyert!")
    elif board[2] == board[5] == board[8] == computer:
        print("A számítógép nyert!")
    elif board[3] == board[6] == board[9] == computer:
        print("A számítógép nyert!")
    elif board[1] == board[5] == board[9] == computer:
        print("A számítógép nyert!")
    elif board[3] == board[5] == board[7] == computer:
        print("A számítógép nyert!")
    else:
        if player_move == 1:
            board[0] = player
        if player_move == 2:
            board[1] = player
        if player_move == 3:
            board[2] = player
        if player_move == 4:
            board[3] = player
        if player_move == 5:
            board[4] = player
        if player_move == 6:
            board[5] = player
        if player_move == 7:
            board[6] = player
        if player_move == 8:
            board[7] = player
        if player_move == 9:
            board[8] = player
        game_proba += 1

game()

input()


      
