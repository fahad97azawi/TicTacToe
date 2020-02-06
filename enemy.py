from Rules import positions
import random

move = None

def computer_move():
    global move
    if True:
        while True:
            rand = random.randrange(0, 9)
            if positions[rand].state:
                move = 1
                positions[rand].state = False
                positions[rand].played = 'circle'
                return positions[rand].x, positions[rand].y
    # else:
    #     while True:
    #         rand = random.randrange(0, 9)
    #         if positions[rand].state:
    #             # move = 1
    #             positions[rand].state = False
    #             positions[rand].played = 'circle'
    #             return positions[rand].x, positions[rand].y
