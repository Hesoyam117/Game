import pygame
import time

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Crusader")

walkRight = [pygame.image.load('right_1.png'),
pygame.image.load('right_2.png'), pygame.image.load('right_3.png'),
pygame.image.load('right_4.png'), pygame.image.load('right_5.png'),
pygame.image.load('right_6.png')]

walkLeft = [pygame.image.load('left_1.png'),
pygame.image.load('left_2.png'), pygame.image.load('left_3.png'),
pygame.image.load('left_4.png'), pygame.image.load('left_5.png'),
pygame.image.load('left_6.png')]

foeWalkLeft = [pygame.image.load('arab_left_1.png'), pygame.image.load('arab_left_2.png'),
pygame.image.load('arab_left_3.png'), pygame.image.load('arab_left_4.png'),
pygame.image.load('arab_left_5.png'), pygame.image.load('arab_left_6.png')]

foeWalkRight = [pygame.image.load('arab_right_1.png'),
pygame.image.load('arab_right_2.png'), pygame.image.load('arab_right_3.png'),
pygame.image.load('arab_right_4.png'), pygame.image.load('arab_right_5.png'),
pygame.image.load('arab_right_6.png')]


arr_r = pygame.image.load('arrow.png')
arr_l = pygame.image.load('arrow_l.png')
arab = pygame.image.load('arab.png')
hp_bar = pygame.image.load('hp_bar.png')
dead = pygame.image.load('dead.png')
dead_scr = pygame.image.load('deadscreen.png')

bg = pygame.image.load('bg.jpg')
bg2 = pygame.image.load('bg_2.jpg')
playerStand = pygame.image.load('idle.png')
wall = pygame.image.load('wall.png')
tower1 = pygame.image.load('tower1.png')
towergain1 = pygame.image.load('towergain1.png')




clock = pygame.time.Clock()

#Координаты объектов на уровне
ob_moving_r = False
ob_moving_l = False
ob_x = 100
ob_x2 = 720
ob_x3 = 990
ob_x4 = 1500
ob_x5 = 1750
wallx = 400
deadend_r = False
deadend_l = False
jumpNo = False
collide_up = False





#Характеристики игрока
x_level = 50
x = 50
y = 435
width = 60
height = 71
speed = 6
hp = 100
death = 0
hpcount = 0
hpcount2 = 0
isJump = False
jumpCount = 10

#levelCount = 0

#Движение игрока
left = False
right = False
animCount = 0
lastMove = "right"

#Характеристики врага
foe_left = True
foe_right = False
foe_animCount = 0
foe_x = 400
foe_y = 435
foe_speed = 3
foe_1 = 400


class arrow():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing

    def draw(self, win):
        if facing == 1:
            win.blit(arr_r, (self.x, self.y))
        else:
            win.blit(arr_l, (self.x, self.y))


        #pygame.draw.circle(win, self.color, (self.x, self.y),
        #self.radius)


def drawWindow():
    global animCount
    global foe_animCount
    win.blit(bg, (0, 0))
    #pygame.draw.rect(win, (0, 255, 0), (ob_x, ob_y, 50, 30))
    #if levelCount == 1:
        #win.blit(bg2, (0, 0))

    win.blit(hp_bar, (20, 20))
    win.blit(wall, (wallx, 347))
    pygame.draw.rect(win, (255, 0, 0), (23, 23, hp, 30))
    #win.blit(arab, (foe_x, foe_y))
    #pygame.draw.rect(win, (255, 0, 0), (ob_x, 200, 50, 30))
    win.blit(tower1, (ob_x, 200))
    #pygame.draw.rect(win, (0, 255, 0), (ob_x2, 350, 80, 40))
    pygame.draw.rect(win, (255, 200, 0), (ob_x3, 400, 70, 20))
    #pygame.draw.rect(win, (255, 0, 0), (ob_x4, 150, 40, 20))
    #pygame.draw.rect(win, (0, 255, 0), (ob_x5, 300, 100, 20))
    #if ob_moving_r == True:
        #ob_x += speed
    #elif ob_moving_l == True:
        #ob_x -= speed


    if animCount + 1 >= 30:
        animCount = 0
    if left:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))
    for bullet in bullets:
        bullet. draw(win)

        #win.blit(dead, (250, 250))
    if foe_animCount + 1 >= 30:
        foe_animCount = 0
    if foe_left == True:
        #foe_right = False
        win.blit(foeWalkLeft[foe_animCount // 5], (foe_x, foe_y))
        foe_animCount += 1
    elif foe_right == True:
        #foe_left = False
        win.blit(foeWalkRight[animCount // 5], (foe_x, foe_y))
        foe_animCount += 1
    else:
        win.blit(arab, (foe_x, foe_y))
    win.blit(towergain1, ((ob_x - 10), 168))

    if hp <= 0:
        death = 1
        win.blit(dead_scr, (0, 0))



    pygame.display.update()

run = True
bullets = []
while run:
    clock.tick(30)
    if ((x + width - 25) <= foe_x and ((x_level >= 1730) or (x_level <= 230))) or ((x + width - 25) <= foe_x and right == False and left == False and ((x_level < 1730) or (x_level > 230))):
        foe_x -= foe_speed
        foe_left = True
        foe_right = False
    elif ((x - width + 25) >= foe_x and ((x_level >= 1730) or (x_level <= 230))) or ((x - width + 25) >= foe_x and right == False and left == False and ((x_level < 1730) or (x_level > 230))):
        foe_x += foe_speed
        foe_right = True
        foe_left = False
    elif ((x_level < 1730) and (x_level > 230)):
        if right == True and (x + 30) >= foe_x:
            foe_x -= (speed - foe_speed)
            foe_right = True
            foe_left = False
        elif left == True and (x + width - 31) <= foe_x :
            foe_x += (speed - foe_speed)
            foe_left = True
            foe_right = False
        elif right == True and (x + width - 31) <= foe_x:
            foe_left = True
            foe_right = False
            foe_x -= (foe_speed + speed)
        elif left == True and (x + 30) >= foe_x:
            foe_right = True
            foe_left = False
            foe_x += (foe_speed + speed)


    if y == foe_y and (((x + width - 25) == foe_x) or ((x - width + 25) == foe_x)):
        if (hp != 0):
            hp -= 5

    if (y == 340 and x < (ob_x3 - 25)) and x > (ob_x3 + 50):
        deadend_l = True
    elif (y == 340 and x > (ob_x3 + 35)):
        deadend_r = True
    elif (y == 140 and x < (ob_x - 26)):
        deadend_l = True
    elif (y == 140 and x > (ob_x + 21)):
        deadend_r = True
    else:
        deadend_l = False
        deadend_r = False
        jumpNo = False

        
    if y == 340 or y == 140:
        jumpNo = True
    else:
        jumpNo = False

#(ob_x3, 400, 70, 20))






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_c]:
        if (x > (ob_x3 - 20) and x < (ob_x3 + 50)) and y == 435:
            y = 340
        elif (x > (ob_x - 20) and x < (ob_x +50)) and y == 435:
            y = 140

    if keys[pygame.K_v ]:
        if (x > (ob_x3 - 20) and x < (ob_x3 + 50)) and y == 340:
            y = 435
        elif (x > (ob_x - 20) and x < (ob_x +50)) and y == 140:
            y = 435


    if keys[pygame.K_l]:
        if hp > 0:
            hp -= 5
    if keys[pygame.K_o]:
        if (hp < 100 and death == 0):
            hp += 5
    if keys[pygame.K_f]:
        if lastMove == "right":
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(arrow(round(x + width // 2), round(y +
            height // 2), 5, (255, 0, 0), facing))

    if keys[pygame.K_a] and x > 10 and x_level > 10:
        if ((x_level > 1730) or (x_level < 230)) and deadend_l != True:
            x_level -= speed
            x -= speed
            left = True
            right = False
            lastMove = "left"
        elif (x_level <= 1730 and x_level >= 230) and deadend_l != True:
            x_level -= speed
            left = True
            right = False
            lastMove = "left"
            ob_moving_r = True
            ob_moving_l = False
            ob_x += speed
            ob_x2 += speed
            ob_x3 += speed
            ob_x4 += speed
            ob_x5 += speed
            wallx += speed



    elif keys[pygame.K_d] and (x < 500 - width - 10) and (x_level < 2000 - width - 10):
        if ((x_level < 230) or (x_level > 1730)) and deadend_r != True:
            x_level += speed
            x += speed
            left = False
            right = True
            lastMove = "right"
        elif (x_level >= 230 and x_level <= 1730) and deadend_r != True:
            x_level += speed
            left = False
            right = True
            lastMove = "right"
            ob_moving_r = False
            ob_moving_l = True
            ob_x -= speed
            ob_x2 -= speed
            ob_x3 -= speed
            ob_x4 -= speed
            ob_x5 -= speed
            wallx -= speed

    else:
        left = False
        right = False
        animCount = 0

    if not(isJump):
        if (keys[pygame.K_w] or keys[pygame.K_SPACE]) and jumpNo == False:
            isJump = True
    else:
        if jumpCount >= -10:# jumpCount 10 - игрок начал прыжок, 0 - середина прыжка - 10 - закончил прыжок
            if jumpCount < 0:#Игрок падает вниз
                y += (jumpCount ** 2) / 2
            else:#Игрок поднимается вверх
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    drawWindow()


pygame.quit()
