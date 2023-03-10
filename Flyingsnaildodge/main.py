import math
import pygame
import random
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Snail Dodge')
clock = pygame.time.Clock()
frame = 1
VEL_x = 0
VEL_y = 0
hp = 3
hit = 0
score = 0

def Player_move(keys_pressed, player_rect, VEL_x, VEL_y):
    if keys_pressed[pygame.K_RIGHT]:  # left
        VEL_x += 1
    if keys_pressed[pygame.K_LEFT]:  # right
        VEL_x -= 1
    if keys_pressed[pygame.K_UP]:  # up
        VEL_y -= 1
    if keys_pressed[pygame.K_DOWN]:  # down
        VEL_y += 1
    VEL_x = VEL_x * 0.95
    VEL_y = VEL_y * 0.95
    player_rect.x += VEL_x
    player_rect.y += VEL_y
    return (VEL_x, VEL_y)

sky = pygame.image.load('Images/sky.jpg').convert()

player = pygame.image.load('Images/player_walk_1.png').convert_alpha()
player_rect = player.get_rect(midbottom=(80, 300))

snail = pygame.image.load('Images/snail.png').convert_alpha()
snail_rect = snail.get_rect(midbottom=(600, 300))
snail_true_y = snail_rect.y

test_font = pygame.font.Font('Images/pixeltype.ttf', 50)
text = test_font.render('HP: 3', False, "Black").convert()
text_rect = text.get_rect(center=(400, 50))

score_text = test_font.render('Score: 0', False, "Black").convert()
score_rect = score_text.get_rect(center=(400, 100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    keys_pressed = pygame.key.get_pressed()
    VEL_x, VEL_y = Player_move(keys_pressed, player_rect, VEL_x, VEL_y)
    if player_rect.top >= 400:
        player_rect.bottom = 0
    elif player_rect.bottom <= 0:
        player_rect.top = 400
    if player_rect.left >= 800:
        player_rect.right = 0
    elif player_rect.right <= 0:
        player_rect.left = 800
    screen.blit(sky, (0, 0))
    screen.blit(player, player_rect)
    text = test_font.render('HP:'+ str(hp), False, "Black").convert()
    screen.blit(text, text_rect)
    score_text = test_font.render('Score: '+ str(score), False, "Black").convert()
    screen.blit(score_text, score_rect)
    snail_rect.x -= math.sqrt(frame)
    if snail_rect.right < 0:
        snail_rect.left = 800
        snail_rect.centery = random.randint(50,350)
        snail_true_y = snail_rect.y
        score += 1
    snail_rect.y = snail_true_y + math.sin(frame) * 100
    screen.blit(snail, (snail_rect.x, snail_rect.y))
    if player_rect.colliderect(snail_rect):
        if hit == 0:
            hp -= 1
            hit = 1
    else:
        hit = 0
    pygame.display.update()
    frame += 0.07
    clock.tick(60)
    if hp == 0:
        exit()
