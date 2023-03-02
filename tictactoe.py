
def displayboard(board):
    print('\n'*100)
    
    print(board[1]+' | ' +board[2]+' | ' +board[3])
    print('----------')
    print(board[4]+' | ' +board[5]+' | ' +board[6])
    print('----------')
    print(board[7]+' | ' +board[8]+' | ' +board[9])

def playerinput():
    marker=''
    while marker not in ['X','O']:
        marker=input(("Player 1, choose your mark 'X' or 'O' ")).upper()
    if marker=='X':
        return ('X','O')
    else:
        return ('O','X')
    
def empty_position(board,position):
    return board[position]==' '

def fullboard(board):
    for i in range(1,10):
        if empty_position(board,i):
            return False
    return True

def marker_placer(board,marker,position):
    board[position]=marker
    
def wingame(marker,board):
    return ((board[1]==board[2]==board[3]==marker)or(board[4]==board[5]==board[6]==marker)or
            (board[7]==board[8]==board[9]==marker)or(board[1]==board[4]==board[7]==marker)or
            (board[2]==board[5]==board[8]==marker)or(board[3]==board[6]==board[9]==marker)or
            (board[1]==board[5]==board[9]==marker)or(board[3]==board[5]==board[7]==marker))

def replay():
    anss=''
    while anss not in ['Y','N']:
        anss=input("Would you like to replay: ").upper()
    return anss== 'Y'

def playerchoice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9]:
        position=int(input("Choose a position between (1 to 9) "))
        if position in range(1,10) and empty_position(board,position):
            return position
        else:
            print('Invalid: Space already taken or invalin Entry !!! ')

def firstchoice():
    import random
    player = random.randint(0,1)
    if player == 0:
        return 'player 1'
    else:
        return 'player 2'
    
print("You are Welcome to Tic-Toc-Toe Game ")
while True:
    

    mboard=[' ']*10
    player_1,player_2= playerinput()

    turn= firstchoice()
    print(f'{turn} will go first! ')

    game=input('Are you ready to play(Y / N): ').upper()[0]

    if game == 'Y':
        game_on=True
    else:
        game_on=False
    
    while game_on:
        if turn == 'player 1':
            
            displayboard(mboard)
            position=playerchoice(mboard)
            marker_placer(mboard,player_1,position)
            if wingame(player_1,mboard):
                displayboard(mboard)
                print('Congratulations !!!, Player 1 wins the game.')
                game_on = False
            else:
                if fullboard(mboard):
                    displayboard(mboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player 2'
        
        else:
            displayboard(mboard)
            position=playerchoice(mboard)
            marker_placer(mboard,player_2,position)
                
            if wingame(player_2,mboard):
                displayboard(mboard)
                print('Congratulations !!!, Player 2 wins the game.')
                game_on = False
            else:
                if fullboard(mboard):
                    displayboard(mboard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'player 1'
    
    if not replay():
        break