import pygame
import random
import mixer

pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
background_img = pygame.image.load('background.jpg')
pygame.display.set_caption('Space Invaders')

mixer.music.load("explosion.wav")
mixer.music.play(-1

ship_img = pygame.image.load('space-invaders.png')
ship_length = 64
shipX = 368
shipY = screen_height-ship_length-25
ship_change = 5

enemy_img = pygame.image.load('enemy.png')
enemy_img=pygame.transform.scale(enemy_img, (40,32))
enemyX = random.randint(0, 734)
enemyY = 50
enemyX_change = 0.6
enemyY_change = 0.6
enemy_width = 40

bullet_img = pygame.image.load('bullet.png')
bullet_img=pygame.transform.scale(bullet_img, (10,10))
bulletY = shipY
bulletX = shipX+ship_length/2-5
bulletY_change = 5

def Player(x,y):
    screen.blit(ship_img,(x,y))

def Enemy(x,y):
    screen.blit(enemy_img, (x, y))

def Move(x):
    global shipX
    if shipX>=0 and shipX<=screen_width-ship_length:
        shipX += x
    elif shipX<0:
        shipX = screen_width-ship_length
    elif shipX > screen_width-ship_length:
        shipX = 0

def bullet(x,y):
    screen.blit(bullet_img, (x, y-10))

def is_collision(enemyX,bulletX,enemy_width,bulletY,enemyY):
    if enemyX<=bulletX<=enemyX+enemy_width and abs(bulletY-enemyY)<33:
        return True
    return False

space_pressed = False
game_running = True
move_right = True
show_score_bool = True
play_again = False
game_over_bool = False

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
scoreX = 10
scoreY = 10

game_over_font = pygame.font.Font('freesansbold.ttf',128)
game_over_X = 300
game_over_Y = 300

def game_over(x,y):
    global game_over_bool
    game_over_screen = font.render('Game Over', True, (255, 255, 255))
    game_over_screen2 = font.render('Your Score is : ' + str(score_value), True, (255, 255, 255))
    play_again_screen = font.render('Press ENTER to play again', True, (255, 255, 255))
    screen.blit(game_over_screen,(x+15,y))
    screen.blit(game_over_screen2,(x-30,y+60))
    screen.blit(play_again_screen,(x-105,y+120))

    game_over_bool = True

def show_score(x,y):
    global score_value
    score = font.render('Score : ' + str(score_value) , True,(255,255,255))
    screen.blit(score,(x,y))

while game_running:

    screen.fill((0,0,0))
    screen.blit(background_img,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if space_pressed== False and game_over_bool== False:
                    space_pressed = True
                    bulletX = shipX+ship_length/2-5
            if event.key == pygame.K_RETURN:
                game_over_bool = False
                enemyX = random.randint(0, 734)
                enemyY = 50
                show_score_bool = True
                score_value = 0
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_LEFT] and game_over_bool== False:
        Move(-ship_change)
    if keystate[pygame.K_RIGHT] and game_over_bool== False:
        Move(ship_change)

    Player(shipX,shipY)
    if (enemyY > screen_height - 2 * ship_length + 2):
        show_score_bool = False
        game_over(game_over_X, game_over_Y)

    if game_over_bool== False:
        enemyY += enemyY_change
        if move_right == True:
            enemyX += enemyX_change
        elif move_right == False:
            enemyX -= enemyX_change
        if enemyX>=screen_width-enemy_width:
            move_right = False
        elif enemyX<=0:
            move_right = True
            enemyX += enemyX_change

        Enemy(enemyX, enemyY)

        if space_pressed == True:
            bulletY -= bulletY_change
            bullet(bulletX,bulletY)
            if bulletY<0:
                space_pressed = False
                bulletY = shipY

        if is_collision(enemyX,bulletX,enemy_width,bulletY,enemyY) == True:
            score_value += 1
            space_pressed = False
            bulletY = shipY
            bulletX = shipX + ship_length / 2 - 5
            enemyX = random.randint(0, 734)
            enemyY = 50
            enemyX_change+=0.4

        if show_score_bool == True:
            show_score(scoreX,scoreY)
    pygame.display.update()

pygame.quit()