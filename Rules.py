from PIL import Image
import pygame
img = Image.open('Tic.png')
places = (42, 17, True), (42, 233, True), (42, 450, True), (258, 17, True), (258, 233, True), (258, 450, True), \
         (464, 17, True), (464, 233, True), (464, 450, True)


class Places:
    def __init__(self, x, y, state, played):
        self.x = x
        self.y = y
        self.state = state
        self.played = played


positions = []
for i in range(0, 9):
    positions.append(Places(places[i][0], places[i][1], places[i][2], None))


def tic_position(mouseX, mouseY):
    posX = posY = None
    for i in range(0, int(img.size[0] * 0.338)):
        for j in range(int(img.size[0] * 0.338), int(img.size[0] * 0.66)):
            if mouseX == i:
                posX = 0.22
                break
            elif mouseX == j:
                posX = 1.33
                break
    if posX is None:
        posX = 2.385
    for i in range(0, int(img.size[1] * 0.33)):
        for j in range(int(img.size[1] * 0.33), int(img.size[1] * 0.68)):
            if mouseY == i:
                posY = 0.28
                break
            elif mouseY == j:
                posY = 3.68
                break
    if posY is None:
        posY = 7.1
    posXX = int(posX * img.size[0] * 0.3)
    posYY = int(posY * img.size[1] * 0.1)
    return int(posXX), int(posYY)


def avail_places():
    mousePos = (tic_position(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
    for obj in positions:
        if mousePos[0] == obj.x and mousePos[1] == obj.y:
            if obj.state:
                obj.state = False
                obj.played = 'cross'
                return True
            else:
                return False


def reset_board():
    for obj in positions:
        obj.state = True
        obj.played = None




def game_won():
    for count in range(0, 7, 3):
        if positions[0 + count].played == positions[1 + count].played == positions[2 + count].played == 'cross':
            return True

    for count in range(0, 3):
        if positions[0 + count].played == positions[3 + count].played == positions[6 + count].played == 'cross':
            return True

    if positions[0].played == positions[4].played == positions[8].played == 'cross' or \
            positions[2].played == positions[4].played == positions[6].played == 'cross':
        return True
