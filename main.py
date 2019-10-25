def position_index():
    print('_1_|_2_|_3_')
    print('_4_|_5_|_6_')
    print(' 7 | 8 | 9 ')

def rules():
    print("1. The game is played on a grid that's 3 squares by 3 squares.")
    print("2. Player 1 is X, Player 2 is O.")
    print("3. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
    print("4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
    print("\nTo enter your mark, input the position index, which are as folows:")
    position_index()

def current_state(lst):
    print('_{}_|_{}_|_{}_          _1_|_2_|_3_'.format(lst[0], lst[1], lst[2]))
    print('_{}_|_{}_|_{}_          _4_|_5_|_6_'.format(lst[3], lst[4], lst[5]))
    print(' {} | {} | {}            7 | 8 | 9 '.format(lst[6], lst[7], lst[8]))

def ask_for_input(player):
    print('enter position player {}:'.format(player))
    position_entered = int(input()) - 1
    # condtion 1 checks if player has enterd a valid position index.
    # condition 2 prevents players from over writing values
    if position_entered not in range(0,9):
        print('invalid input. choose a number from 1 - 9')
        ask_for_input(player)
    elif lst[position_entered] != ' ':
        print('invalid input. this position is already filled.')
        ask_for_input(player)
    else:
        if player == 1:
           lst[position_entered ] = 'X'
        else:
            lst[position_entered] = 'O'
        current_state(lst)

def check_winner():
    #rows
    if (lst[0] == lst[1] == lst[2] != ' ') or (lst[3] == lst[4] == lst[5] != ' ') or (lst[6] == lst[7] == lst[8] != ' '):
       return True
    #columns
    elif (lst[0] == lst[3] == lst[6] != ' ') or (lst[1] == lst[4] == lst[7] != ' ') or (lst[2] == lst[5] == lst[8] != ' '):
        return True
    #diagonas
    elif (lst[0] == lst[4] == lst[8] != ' ') or (lst[2] == lst[4] == lst[6] != ' '):
        return True
    else:
        return False

print('\nwelcome to the tic tac to game\n')
rules()
lst = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]
winner = 'None'
for i in range(9):
    if i%2 == 0:
        ask_for_input(1)
    else:
        ask_for_input(2)
    if check_winner():
        winner = '1' if (i%2 == 0) else '2'
        break

print('game over')
if winner == '1' or winner == '2':
    print('player {} wins!'.format(winner))
else:
    print('its a tie')