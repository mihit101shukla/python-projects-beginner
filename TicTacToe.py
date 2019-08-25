import random

def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    marker = ''

    while marker != 'x' and marker != 'o':
        marker = input('Player 1 choose either x or o: ').lower()
        player1 = marker.upper()
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'
    return player1, player2

def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return True
    else:
        pass


def choose_first():
    x = random.randint(1,2)
    if x==1:
        return 'player1'
    else:
        return 'player2'


def space_check(board, position1):
    if board[position1] == 'X' or board[position1] == 'O':
        return False
    else:
        return True


def full_board_check(board):
    for char in range(1,10):
        if space_check(test_board, char):
            return False
    return True


def player_choice(board):
    while True:
        position2 = input('What is your next position(1-9)?: ')
        if position2 in '123456789':
            position2 = int(position2)
        else:
            print('That is not a number, try again! ')
            continue
        if space_check(board, position2):
            return position2
        else:
            continue


def replay():
    x = input('Do you want to play again?: ')
    if x.lower() == 'yes':
        return True
    elif x.lower() == 'no':
        return False
    else:
        pass

while True:
    print('\n' *100)
    test_board = [' '] * 10
    game_on = input('Welcome to Tic Tac Toe! Do you want to play? ').lower()
    if game_on != 'yes':
        break
    p1mark, p2mark = player_input()
    turn = choose_first()
    print(turn + ' will go first for this round')

    while game_on == 'yes':
        if turn == 'player1':
            print("\nIt is currently player one's turn")
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, p1mark, position)
            print('\n'*20)
            if win_check(test_board, p1mark):
                display_board(test_board)
                print('PLAYER 1 WINS, GOOD GAME!')
                break
            elif full_board_check(test_board) == True:
                display_board(test_board)
                print('TIE GAME')
                break
            else:
                turn = 'player2'

        if turn == 'player2':
            print("\nIt is currently player two's turn")
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, p2mark, position)
            print('\n'*20)
            if win_check(test_board, p2mark):
                display_board(test_board)
                print('PLAYER 2 WINS, GOOD GAME!')
                break
            elif full_board_check(test_board) == True:
                display_board(test_board)
                print('TIE GAME')
                break
            else:
                turn = 'player1'

        else:
            break
    if not replay():
        break
