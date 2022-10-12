import pygame
from sys import exit
pygame.init()

class Invader(object):

    def __init__(self, rect):
        self.rect = rect


class Player(object):

    def __init__(self, rect):
        self.rect = rect


size = (800, 600)
black = (0, 0, 0)
screen = pygame.display.set_mode(size)
invader_img = pygame.image.load('invader.png')
player_img = pygame.image.load('tank.png')
pygame.key.set_repeat(20, 20)
invader_layout = []

for x in range(0, 9):
    invader_layout.append([])
    for y in range(0, 6):
        invader_rect = pygame.Rect((60 * (x + 1), 10 + y * 40, 50, 50))
        invader_layout[x].append(Invader(invader_rect))
player = Player(pygame.Rect((350, 540, 50, 50)))

x_speed = [4, 0]
y_speed = [0, 3]
player_move_right = [15, 0]
player_move_left = [-15, 0]
enemy_movement = x_speed
counter = 0
reverse_direction = False

while True:
    if counter != 0:
        counter -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player.rect[0] > 5:
                player.rect = player.rect.move(player_move_left)
            if event.key == pygame.K_RIGHT and player.rect[0] < 740:
                player.rect = player.rect.move(player_move_right)

    for row in invader_layout:
        for invader in row:
            invader.rect = invader.rect.move(enemy_movement)
            if enemy_movement == x_speed and (
                  invader.rect.left < 5 or invader.rect.right > size[0] - 5):
                reverse_direction = True
            if invader.rect.bottom >= 600:
                exit()

    if reverse_direction == True:
        x_speed[0] *= -1
        enemy_movement = y_speed
        reverse_direction = False
        counter = 10
    if counter == 0:
        enemy_movement = x_speed

    screen.fill(black)
    for row in invader_layout:
        for invader in row:
            screen.blit(invader_img, invader.rect)
    screen.blit(player_img, player.rect)
    pygame.display.flip()