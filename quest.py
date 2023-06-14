from random import randint, choice

SIZE_X = randint(5, 20)
SIZE_Y = randint(5, 20)


def check_state(objects):

    for obj in objects:
        if obj['type'] == 'char':
            char = obj

        elif obj['type'] == 'portal':
            portal = obj

        elif obj['type'] == 'enemy':
            lose_condition = char['x'] == obj['x'] and char['y'] == obj['y']

            if lose_condition:
                char['sign'] = 'L'
                print(f'You loser! Your turns {turns}')
                break

    win_condition = char['x'] == portal['x'] and char['y'] == portal['y']


    if win_condition:
        char['sign'] = 'W'
        print(f'You won! Your turns {turns}')


    return win_condition or lose_condition


def generate_map(objects, size_x=SIZE_X, size_y=SIZE_Y):

    world_map = []

    for j in range(size_y):
        row = []

        for i in range(size_x):
            row.append(' ')

        world_map.append(row)

    for obj in objects:
        world_map[obj['y']][obj['x']] = obj['sign']

    return world_map


def move(direction, obj, size_x=SIZE_X, size_y=SIZE_Y):

    if direction == 'w' and obj['y'] > 0:
        obj['y'] -= 1
    elif direction == 'a' and obj['x'] > 0:
        obj['x'] -= 1
    elif direction == 's' and obj['y'] < size_y - 1:
        obj['y'] += 1
    elif direction == 'd' and obj['x'] < size_x - 1:
        obj['x'] += 1



def print_map(world_map):
    for row in world_map:
        print(f'|{"|".join(row)}|')


char = {'x': randint(0, SIZE_X - 1),
        'y': randint(0, SIZE_Y - 1),
        'sign': 'X',
        'type': 'char'}

enemy = {'x': randint(0, SIZE_X - 1),
         'y': randint(0, SIZE_Y - 1),
         'sign': 'T',
         'type': 'enemy'}

portal = {'x': randint(0, SIZE_X - 1),
          'y': randint(0, SIZE_Y - 1),
          'sign': 'O',
          'type': 'portal'}


objects = [char, enemy, portal]

turns = 0


while True:

    end_flag = check_state(objects)
    world_map = generate_map(objects)
    print(world_map)

    if end_flag:
        break

    for obj in objects:
        if obj['type'] == 'char':
            direction = input('Enter direction (w, a, s, d): ')

        elif obj['type'] == 'enemy':
            enemy_direction = choice('wasd')

        move(direction, obj)

    turns += 1



