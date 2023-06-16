def queen_move(r, c, is_captured=False):
    possible_attack = []
    for move in positions:
        row_col = (r + move[0], c + move[1])
        row, col = row_col
        while valid_position(row, col):
            if matrix[row][col] == 'Q':
                break
            elif matrix[row][col] == 'K':
                possible_attack.append((row, col))
                break
            row += move[0]
            col += move[1]

    return possible_attack


def valid_position(r, c):
    return 0 <= r < SIZE and 0 <= c < SIZE


SIZE = 8
matrix = [input().split() for _ in range(SIZE)]
queens = []
king = []
positions = [
    (+1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (1, -1),
    (1, 1),
    (-1, -1),
    (-1, 1),
]

for row in range(SIZE):
    for col in range(SIZE):
        if matrix[row][col] == "Q":
            queens.append((row, col))
        if matrix[row][col] == "K":
            king = (row, col)
king_is_down = False

capturing_queens = []
for queen in queens:
    row, col = queen
    queen_position = queen_move(row, col)
    if queen_position:
        capturing_queens.append(queen)

if capturing_queens:
    for one in capturing_queens:
        print([*one])
else:
    print("The king is safe!")
