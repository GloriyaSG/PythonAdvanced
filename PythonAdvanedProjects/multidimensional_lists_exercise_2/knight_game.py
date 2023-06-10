size_of_board = int(input())
matrix = [list(input()) for x in range(size_of_board)]

possible_moves = {
    (-2,1),  # two_up, one_left,
    (-2,-1),  # two up, one right
    (2,1),  # two down, one left
    (2,-1),  # two down, one right
    (-1,-2),  # one left, two up
    (-1,2),  # one left, two down
    (1,2),  # one right, two down
    (1,-2),  # one left, two up
}
knight_to_remove = 0

while True:
    max_attack = 0
    position_of_knights = []
    for row in range(size_of_board):
        for col in range(size_of_board):

            if matrix[row][col] == "K":
                attack = 0
                for position in possible_moves:

                    position_row = position[0] + row
                    position_col = position[1] + col

                    if 0 <= position_row < size_of_board and 0 <= position_col < size_of_board:

                        if matrix[position_row][position_col] == "K":
                            attack += 1
                if attack > max_attack:
                    max_attack = attack
                    position_of_knights = [row,col]

    if len(position_of_knights) != 0:
        pos_r, pos_c = position_of_knights
        matrix[pos_r][pos_c] = "O"
        knight_to_remove += 1
    else:
        break
print(knight_to_remove)

