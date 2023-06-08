from random import randint, choice

SIZE_X = randint(5, 20)
SIZE_Y = randint(5, 20)


def check_state(char_x, char_y, char_sign,
                exit_x, exit_y,
                enemy_x, enemy_y):

    win_condition = char_x == exit_x and char_y == exit_y
    lose_condition = char_x == enemy_x and char_y == enemy_y

    if win_condition:
        char_sign = 'W'
        print(f'You won! Your turns {turns}')

    elif lose_condition:
        char_sign = 'L'
        print(f'You loser! Your turns {turns}')

    return char_sign, win_condition or lose_condition


def generate_map(char_x, char_y, char_sign,
                 enemy_x, enemy_y, enemy_sign,
                 exit_x, exit_y,
                 size_x=SIZE_X, size_y=SIZE_Y):

    world_map = ''

    for j in range(size_y):
        row = '|'

        for i in range(size_x):

            if char_x == i and char_y == j:
                row += f'{char_sign}|'

            elif exit_x == i and exit_y == j:
                row += 'O|'

            elif enemy_x == i and enemy_y == j:
                row += f'{enemy_sign}'

            else:
                row += ' |'

        world_map += f'{row}\n'

    return world_map


def move(direction, x, y, size_x=SIZE_X, size_y=SIZE_Y):

    if direction == 'w' and y > 0:
        y -= 1
    elif direction == 'a' and x > 0:
        x -= 1
    elif direction == 's' and y < size_y - 1:
        y += 1
    elif direction == 'd' and x < size_x - 1:
        x += 1

    return x, y


char_x = randint(0, SIZE_X - 1)
char_y = randint(0, SIZE_Y - 1)
char_sign = 'X'

exit_x = randint(0, SIZE_X - 1)
exit_y = randint(0, SIZE_Y - 1)

enemy_x = randint(0, SIZE_X - 1)
enemy_y = randint(0, SIZE_X - 1)
enemy_sign = 'T|'

turns = 0


while True:

    char_sign, end_flag = check_state(char_x, char_y, char_sign,
                            exit_x, exit_y,
                            enemy_x, enemy_y)

    world_map = generate_map(char_x, char_y, char_sign,
                             enemy_x, enemy_y, enemy_sign,
                             exit_x, exit_y)
    print(world_map)

    if end_flag:
        break

    direction = input('Enter direction (w, a, s, d): ')
    char_x, char_y = move(direction, char_x, char_y)

    enemy_direction = choice('wasd')
    enemy_x, enemy_y = move(enemy_direction, enemy_x, enemy_y)

    turns += 1



