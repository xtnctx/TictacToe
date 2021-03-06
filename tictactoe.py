
''' Use your NumPad to play the game '''

board_sample = f'\
|     7     |     8     |     9     | \n\
------------------------------------- \n\
|     4     |     5     |     6     | \n\
------------------------------------- \n\
|     1     |     2     |     3     |'

# //////////////// Winning Moves ////////////////
win_horizontal = [
    [6, 7, 8],
    [3, 4, 5],
    [0, 1, 2]
]

win_vertical = [
    [6, 3, 0],
    [7, 4, 1],
    [8, 5, 2]
]

win_diagonal = [
    [6, 4, 2],
    [8, 4, 0]
]

winning_moves = [win_horizontal, win_vertical, win_diagonal]
# //////////////////////////////////////////////

def checkWinner(player: int) -> bool:
    for win in winning_moves:
        for i in range(len(win)):
            point = 0
            for choices in player:
                if choices in win[i]:
                    point += 1
                if point == 3: return True
    return False

segment = ['']*9
segment_player1 = []
segment_player2 = []

while True:
    player1 = int(input("Player1's turn: "))
    segment[player1-1] = 'X'
    segment_player1.append(player1-1)
    board = f'\
    |     {segment[6]}     |     {segment[7]}     |     {segment[8]}     | \n\
    ----------------------------------- \n\
    |     {segment[3]}     |     {segment[4]}     |     {segment[5]}     | \n\
    ----------------------------------- \n\
    |     {segment[0]}     |     {segment[1]}     |     {segment[2]}     |'

    print(board)

    if checkWinner(segment_player1):
        print('\nPlayer1 Wins!')
        break

    player2 = int(input("Player2's turn: "))
    segment[player2-1] = 'O'
    segment_player2.append(player2-1)
    board = f'\
    |     {segment[6]}     |     {segment[7]}     |     {segment[8]}     | \n\
    ----------------------------------- \n\
    |     {segment[3]}     |     {segment[4]}     |     {segment[5]}     | \n\
    ----------------------------------- \n\
    |     {segment[0]}     |     {segment[1]}     |     {segment[2]}     |'

    print(board)

    if checkWinner(segment_player2):
        print('\nPlayer2 Wins!')
        break
