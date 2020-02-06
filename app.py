import pygame
# from PIL import Image
from Rules import tic_position, avail_places, reset_board, positions, game_won
import time
from enemy import computer_move

pygame.init()
screen = pygame.display.set_mode((649, 660))
background = pygame.image.load('Tic.png')
screen.blit(background, (0, 0))
myFont = pygame.font.SysFont(None, 25, True)
games_played = myFont.render('Games played: ', True, (255, 255, 255), (0, 0, 0))
cross = pygame.image.load('cross.png')
circle = pygame.image.load('circle.png')
screen.blit(games_played, (10, 640))
games_played_num = 0


running = True
turn = 0
while running:
    games_played_txt = myFont.render(f'{games_played_num}', True, (255, 255, 255), (0, 0, 0))
    screen.blit(games_played_txt, (155, 640))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif turn == 9 or game_won():
            time.sleep(0.2)
            if game_won():
                games_played_num += 1
            reset_board()
            screen.blit(background, (0, 0))

            turn = 0

        elif turn % 2 == 0 and turn <= 8:
            if pygame.mouse.get_pressed()[0] and avail_places():
                screen.blit(cross, (tic_position(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])))
                turn += 1
                for obj in positions:
                    print(obj.x, obj.y, obj.state, obj.played)
                print('\n')
        elif turn % 2 == 1 and turn <= 8:
            x, y = computer_move()
            screen.blit(circle, (x, y))
            turn += 1

    pygame.display.set_caption('TicTacToe')
    pygame.display.update()
