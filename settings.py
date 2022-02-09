FONT_NAME = "Calibri"
PLAYER_IDS = ['X', 'O']
X_WINDOW = 500
Y_WINDOW = 500

SEGMENT_GRID_SPACING = 6
SEGMENT_BTN_FONT_SIZE = 65
BTN_FONT_SIZE = 12
BTN_V_MIN = 50

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

WINNING_MOVES = [win_horizontal, win_vertical, win_diagonal]
# //////////////////////////////////////////////