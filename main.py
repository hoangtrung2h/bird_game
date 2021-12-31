import pygame
import random
import math
import time
# create screen

pygame.init()
screen = pygame.display.set_mode((800, 700))

# icon and name of game
icon= pygame.image.load('parrot.png')
pygame.display.set_icon(icon)

# player
player_image = pygame.image.load("macaw.png")
player_change = 0.3
player_X = 100
player_Y = 420


def player(x, y):
    screen.blit(player_image, (x, y))


# target
targetImage = pygame.image.load("corn.png")
target_image = []
target_X = []
target_Y = []
target_change = []
target_display=[]
number_of_target=6

for i in range(number_of_target):
    target_image.append(targetImage)
    target_X.append(random.randint(500, 700))
    target_Y.append(random.randint(50, 600))
    target_change.append(0.3)
    target_display.append(True)

def target(x, y, i):
    screen.blit(target_image[i], (x, y))


# bullet
bulletImage = pygame.image.load("seeds.png")
bullet_image = []
number_of_bullet=3
bullet_X = []
bullet_Y = []
bullet_change = []
bullet_status = []
for i in range(number_of_bullet):
    bullet_image.append(bulletImage)
    bullet_X.append(100)
    bullet_Y.append(0)
    bullet_status.append("ready")
    bullet_change.append(0.5)


def bullet(x, y, i):
    screen.blit(bullet_image[i], (x, y))
# collision


def collision(bullet_x, bullet_y, player_x, player_y):
    distance = math.sqrt((bullet_x-player_x)**2+(bullet_y-player_y)**2)
    check_collision = False
    if distance < 40:
        check_collision = True
    return check_collision

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
def show_score():
    score=font.render("SCORE: "+str(score_value),True,(123,123,123))
    screen.blit(score,(textX,textY))
# winner
font_winner= pygame.font.Font('freesansbold.ttf', 64)

def show_winner():
    winner=font_winner.render("YOU ARE WiNNER",True,(100,100,100))
    screen.blit(winner,(100,300))
# Loop game
Running = True
while Running:
    screen.fill((40, 116, 166))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_change = -0.5
            if event.key == pygame.K_SPACE:
                for i in range(number_of_bullet):
                    if bullet_status[i] == "ready":
                        bullet_Y[i] = player_Y
                        bullet_status[i] = "fire"
                        break
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player_change = 0.3

    player_Y += player_change
    # player
    if player_Y > 650:
        player_Y = 650
    if player_Y < 10:
        player_Y = 10
    
    # target
    for i in range(number_of_target):
        if target_display[i]==True:
            target_Y[i]+=target_change[i]
        if target_Y[i]<30:
            target_change[i]=0.3
        if  target_Y[i]>650:
            target_change[i]=-0.3
        
        target(target_X[i],target_Y[i],i)
    # check collision
        for j in range (number_of_bullet):
            if collision(bullet_X[j],bullet_Y[j],target_X[i],target_Y[i]):
                bullet_status[j]="ready"
                bullet_X[j]=player_X
                target_Y[i]=2000               
                score_value+=1
                target_display[i]=False
    # bullet
    for i in range(number_of_bullet):
        if bullet_X[i] > 700:
            bullet_X[i] = 100
            bullet_status[i] = "ready"
        if bullet_status[i] == "fire":
            bullet_X[i] += bullet_change[i]
            bullet(bullet_X[i], bullet_Y[i], i)
    if score_value==6:
        player_Y=2000
        player_change=0
        show_winner()
    show_score()
    player(player_X, player_Y)
    pygame.display.update()
    
