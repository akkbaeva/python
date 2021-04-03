the_board = {
    '1': '','2': '','3': '',
    '4': '','5': '','6': '',
    '7': '','8': '','9': '',
}
board_keys = []
for key in the_board:
    board_keys.append(key)

def paint_board(board):
    print('---------')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('---------')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('---------')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('---------')

def game():
    turn = 'X'
    count = 0

    for key in range(10):
        paint_board(the_board)    
        print('it is your turn' + turn  + 'to which position')
        
        move = input('')

        if the_board[move] == '':
            the_board[move] = turn 
            count += 1
        else:
            print('that positision is filled , please choose another one')
            continue

        if count >= 5:
            if the_board['1'] == the_board['2'] == the_board['3'] != '':
                paint_board(the_board)
                print('Game over')
                print(turn, 'won')
                break
            if the_board['4'] == the_board['5'] == the_board['6'] != '':
                paint_board(the_board)
                print('Game over')
                print(turn, 'won')
                break
            if the_board['7'] == the_board['8'] == the_board['9'] != '':
                paint_board(the_board)
                print('Game over')
                print(turn, 'won')
                break
            if the_board['1'] == the_board['4'] == the_board['7'] != '':
                paint_board(the_board)
                print('Game over')
                print(turn, 'won')
                break
            if the_board['2'] == the_board['5'] == the_board['8'] != '':
                paint_board(the_board)
                print('Game over')
                print(turn, 'won')
                break
            if the_board['3'] == the_board['6'] == the_board['9'] != '':
                paint_board(the_board)
                print('Game over')
                print(turn, 'won')
                break
            if the_board['1'] == the_board['5'] == the_board['9'] != '':
                paint_board(the_board)
                print('Game over')
                print(turn, 'won')
                break
            if the_board['3'] == the_board['5'] == the_board['7'] != '':
                paint_board(the_board)
                print('Game over')
                print(turn, 'won')
                break
        if count == 9:
            print('Game over')
            print('No one wins')

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    restart = input('restart or stop? ')
    if restart == 'yes' or restart == 'YES':
        for key  in board_keys:
            the_board[key] = ''
        game()

game()
