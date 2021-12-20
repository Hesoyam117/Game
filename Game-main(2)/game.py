import pygame
import time

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Crusader")

walkRight = [pygame.image.load('Textures/right_1.png'),
pygame.image.load('Textures/right_2.png'), pygame.image.load('Textures/right_3.png'),
pygame.image.load('Textures/right_4.png'), pygame.image.load('Textures/right_5.png'),
pygame.image.load('Textures/right_6.png')]

walkLeft = [pygame.image.load('Textures/left_1.png'),
pygame.image.load('Textures/left_2.png'), pygame.image.load('Textures/left_3.png'),
pygame.image.load('Textures/left_4.png'), pygame.image.load('Textures/left_5.png'),
pygame.image.load('Textures/left_6.png')]

attack = [pygame.image.load('Textures/attack_1.png'),
pygame.image.load('Textures/attack_2.png'), pygame.image.load('Textures/attack_3.png'),
pygame.image.load('Textures/attack_4.png'), pygame.image.load('Textures/attack_5.png'),
pygame.image.load('Textures/attack_6.png')]

attackleft = [pygame.image.load('Textures/attackleft_1.png'),
pygame.image.load('Textures/attackleft_2.png'), pygame.image.load('Textures/attackleft_3.png'),
pygame.image.load('Textures/attackleft_4.png'), pygame.image.load('Textures/attackleft_5.png'),
pygame.image.load('Textures/attackleft_6.png')]


foeWalkLeft = [pygame.image.load('Textures/arab_left_1.png'), pygame.image.load('Textures/arab_left_2.png'),
pygame.image.load('Textures/arab_left_3.png'), pygame.image.load('Textures/arab_left_4.png'),
pygame.image.load('Textures/arab_left_5.png'), pygame.image.load('Textures/arab_left_6.png')]

foeWalkRight = [pygame.image.load('Textures/arab_right_1.png'),
pygame.image.load('Textures/arab_right_2.png'), pygame.image.load('Textures/arab_right_3.png'),
pygame.image.load('Textures/arab_right_4.png'), pygame.image.load('Textures/arab_right_5.png'),
pygame.image.load('Textures/arab_right_6.png')]

climbingAnim = [pygame.image.load('Textures/climbing1.png'),
pygame.image.load('Textures/climbing2.png'), pygame.image.load('Textures/climbing3.png'),
pygame.image.load('Textures/climbing4.png'), pygame.image.load('Textures/climbing5.png'),
pygame.image.load('Textures/climbing6.png')]

archer_left = pygame.image.load('Textures/archer.png')
archer_right = pygame.image.load('Textures/archer_right.png')

deadbody = pygame.image.load('Textures/deadbody.png')


arr_r = pygame.image.load('Textures/arrow.png')
arr_l = pygame.image.load('Textures/arrow_l.png')
arab = pygame.image.load('Textures/arab.png')
hp_bar = pygame.image.load('Textures/hp_bar.png')
dead_scr = pygame.image.load('Textures/deadscreen.png')

bg = pygame.image.load('Textures/bg.jpg')
bg2 = pygame.image.load('Textures/bg_2.jpg')
playerStand = pygame.image.load('Textures/idle.png')
wall = pygame.image.load('Textures/wall.png')
tower1 = pygame.image.load('Textures/tower1.png')
towergain1 = pygame.image.load('Textures/towergain1.png')
idle_left = pygame.image.load('Textures/left_1.png')
ladder = pygame.image.load('Textures/ladder.png')
ladder2 = pygame.image.load('Textures/ladder.png')



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
ladderx = 530
ladderx2 = 1050
############
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
attacking = False
damaging = False

#levelCount = 0

#Движение игрока
left = False
right = False
animCount = 0
animCount_a = 0
lastMove = "right"
moving = False
climbing = False
climb_animCount = 0


#Характеристики врага
###Враг1
foe_left = True
foe_right = False
foe_animCount = 0
foe_x = 400
foe_y = 435
deadbody_x = 0
foe_speed = 3
foe_hp = 3
foe_dead = False
deadbody_x = 0
####
#Враг2
foe1_left = True
foe1_right = False
foe1_animCount = 0
foe1_x = 1750
foe1_y = 435
#deadbody_x = 0
foe1_hp = 3
foe1_dead = False
foe1_speed = 4
archer_x = 800
archer_y = 334
archerL = True
archerR = False





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
    global deadbody_x
    global animCount_a
    global climb_animCount
    global archerL
    global archerR

###Отрисовка объектов в игре
    win.blit(bg, (0, 0))
    #pygame.draw.rect(win, (0, 255, 0), (ob_x, ob_y, 50, 30))
    #if levelCount == 1:
        #win.blit(bg2, (0, 0))

    win.blit(hp_bar, (20, 20))
    win.blit(wall, (wallx, 347))
    win.blit(ladder, (ladderx, 408))
    win.blit(ladder2, (ladderx2, 408))
    pygame.draw.rect(win, (255, 0, 0), (23, 23, hp, 30))
    #win.blit(arab, (foe_x, foe_y))
    #pygame.draw.rect(win, (255, 0, 0), (ob_x, 200, 50, 30))
    win.blit(tower1, (ob_x, 200))
    #pygame.draw.rect(win, (0, 255, 0), (ob_x2, 350, 80, 40))
    #pygame.draw.rect(win, (255, 200, 0), (ob_x3, 400, 70, 20))
    #pygame.draw.rect(win, (255, 0, 0), (ob_x4, 150, 40, 20))
    #pygame.draw.rect(win, (0, 255, 0), (ob_x5, 300, 100, 20))
    #if ob_moving_r == True:
        #ob_x += speed
    #elif ob_moving_l == True:
        #ob_x -= speed
    #deadbody_x = foe_x
    if foe_dead == True:
        #deadbody_x = foe_x
        win.blit(deadbody, (foe_x, 460))

###


###Анимация ГГ
    if animCount + 1 >= 30:
        animCount = 0
    #if animCount_a + 1 >= 30:
        #animCount_a = 0

    animCount_a = 0
    if animCount_a + 1 >= 30:
        animCount_a = 0
    elif lastMove == "right" and attacking == True:
        win.blit(attack[animCount_a // 5], (x, y))
        animCount_a += 1
    elif lastMove != "right" and attacking == True:
         win.blit(attackleft[animCount_a // 5], (x, y))
         animCount_a += 1
    if left == True and attacking == False:
        win.blit(walkLeft[animCount // 5], (x, y))
        animCount += 1
    elif right == True and attacking == False:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    if attacking == False and moving == False:
        if lastMove == "right":
             win.blit(playerStand, (x, y))
        else:
            win.blit(idle_left, (x, y))
    for bullet in bullets:
        bullet. draw(win)
    if climb_animCount + 1 >= 30:
        climb_animCount = 0
    if climbing == True:
        win.blit(climbingAnim[climb_animCount // 5], (x, y))

###




###Анимация врага
    if archerR == True:
        win.blit(archer_right, (archer_x, archer_y))
    elif archerL == True:
        win.blit(archer_left, (archer_x, archer_y))
    if foe_animCount + 1 >= 30:
        foe_animCount = 0
    if foe_left == True:
        #foe_right = False
        win.blit(foeWalkLeft[foe_animCount // 5], (foe_x, foe_y))
        foe_animCount += 1
    elif foe_right == True:
        #foe_left = False
        win.blit(foeWalkRight[foe_animCount // 5], (foe_x, foe_y))
        foe_animCount += 1
    else:
        win.blit(arab, (foe_x, foe_y))
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
#Враг2
    #global foe1_animCount
    #global foe1_x
    #global foe1_y
    #global foe1_right
    #global foe1_left
    #if foe1_animCount + 1 >= 30:
        #foe1_animCount = 0
    #if foe1_left == True:
        #foe1_right = False
        #win.blit(foeWalkLeft[foe1_animCount // 5], (foe1_x, foe1_y))
        #foe1_animCount += 1
    #elif foe_right == True:
        #foe1_left = False
        #win.blit(foeWalkRight[foe1_animCount // 5], (foe1_x, foe1_y))
        #foe1_animCount += 1
    #else:
        #win.blit(arab, (foe1_x, foe1_y))
########


    win.blit(towergain1, ((ob_x - 10), 168))
    pygame.draw.rect(win, (255, 0, 0), ((foe_x + 20), foe_y, (foe_hp * 5), 5))



    if hp <= 0:
        death = 1
        win.blit(dead_scr, (0, 0))




###



    pygame.display.update()

run = True
bullets = []
while run:
    clock.tick(30)
    print(x, x_level, y)


###Ограничения при передвижении для игрока
    if (y == 140 and x < (ob_x - 26)):
            deadend_l = True
    elif (y == 140 and x > (ob_x + 21)):
            deadend_r = True
    elif y < 344 and x < wallx - 25:
            deadend_l = True
    elif y < 344 and x > (wallx + 1350):
            deadend_r = True
            #y = 435
            #x = (wallx + 1425)
            #ob_x -= 75
            #ob_x2 -= 75
            #ob_x3 -= speed
            #ob_x4 -= 75
            #ob_x5 -= 75
            #wallx -= 75
            #ladderx -= 75
            #ladderx2 -= 75
            #foe_x -= 75
            #foe1_x -= 75

    else:
            deadend_l = False
            deadend_r = False
            jumpNo = False

    if y == 140: #y == 340)
            jumpNo = True
    else:
            jumpNo = False
###



###Поведение врага в игре
###Лучник
    if x < archer_x:
        archerL = True
        archerR = False
    else:
        archerR = True
        archerL = False
    if y > 332 and y < 334:
        if len(bullets) < 5:
            bullets.append(arrow(round(archer_x + width // 2), round(archer_y +
            height // 2), 5, (255, 0, 0), facing))
#Враг1
    if ((x + width - 25) <= foe_x and ((x_level >= 1730) or (x_level <= 230))) or ((x + width - 25) <= foe_x and right == False and left == False and ((x_level < 1730) or (x_level > 230))):
        if foe_hp > 0:
            foe_x -= foe_speed
            foe_left = True
            foe_right = False
    elif ((x - width + 25) >= foe_x and ((x_level >= 1730) or (x_level <= 230))) or ((x - width + 25) >= foe_x and right == False and left == False and ((x_level < 1730) or (x_level > 230))):
        if foe_hp > 0:
            foe_x += foe_speed
            foe_right = True
            foe_left = False
    elif ((x_level < 1730) and (x_level > 230)):
        if foe_hp > 0:
             if right == True and (x + 30) >= foe_x and deadend_l != True and deadend_r != True:
                 foe_x -= (speed - foe_speed)
                 foe_right = True
                 foe_left = False
             elif left == True and (x + width - 31) <= foe_x and deadend_l != True and deadend_r != True:
                 foe_x += (speed - foe_speed)
                 foe_left = True
                 foe_right = False
             elif right == True and (x + width - 31) <= foe_x and deadend_l != True and deadend_r != True:
                 foe_left = True
                 foe_right = False
                 foe_x -= (foe_speed + speed)
             elif left == True and (x + 30) >= foe_x and deadend_l != True and deadend_r != True:
                 foe_right = True
                 foe_left = False
                 foe_x += (foe_speed + speed)
    hitCount = 0
    danger = 0
    if (x + width - 25 == foe_x and y == foe_y) or ((x - width + 20) == foe_x and y == foe_y):
        danger = 1
        while hp != 0:
            if danger == 1 and hp != 0:
                hp -= 10
                break
    elif foe_hp <= 0:
        foe_y = 500
        foe_dead = True
    elif foe_hp > 0:
        foe_y = 435
        foe_dead = False
##########################################################################################################################################
##########################################################################################################################################
##########################################################################################################################################
#Враг2
    infov1 = False
    if foe1_x < 500  and foe1_x > 0:
        infov1 = True
    elif ((x + width - 25) <= foe1_x and ((x_level >= 1730) or (x_level <= 230))) or ((x + width - 25) <= foe1_x and right == False and left == False and ((x_level < 1730) or (x_level > 230))):
        if foe1_hp > 0 and infov1 == True:
            foe1_x -= foe1_speed
            foe1_left = True
            foe1_right = False
        elif (infov1 == False and x_level < 1500 and foe1_x < 1750):
            foe_right = True
            foe1_x += foe1_speed
    elif ((x - width + 25) >= foe1_x and ((x_level >= 1730) or (x_level <= 230))) or ((x - width + 25) >= foe1_x and right == False and left == False and ((x_level < 1730) or (x_level > 230))):
        if foe1_hp > 0 and infov1 == True:
            foe1_x += foe1_speed
            foe1_right = True
            foe1_left = False
        elif (infov1 == False and x_level < 1500 and foe1_x < 1750):
            foe1_x += foe1_speed
            foe_right = True
    elif ((x_level < 1730) and (x_level > 230)):
        if foe1_hp > 0 and infov1 == True:
             if right == True and (x + 30) >= foe1_x and deadend_l != True and deadend_r != True:
                 foe1_x -= (speed - foe1_speed)
                 foe1_right = True
                 foe1_left = False
             elif left == True and (x + width - 31) <= foe_x and deadend_l != True and deadend_r != True:
                 foe1_x += (speed - foe1_speed)
                 foe1_left = True
                 foe1_right = False
             elif right == True and (x + width - 31) <= foe1_x and deadend_l != True and deadend_r != True:
                 foe1_left = True
                 foe1_right = False
                 foe1_x -= (foe1_speed + speed)
             elif left == True and (x + 30) >= foe1_x and deadend_l != True and deadend_r != True:
                 foe1_right = True
                 foe1_left = False
                 foe1_x += (foe1_speed + speed)
             elif (infov1 == False and x_level < 1500 and foe1_x < 1750):
                 foe1_x += foe1_speed
                 foe_right = True

    #hitCount = 0
    #danger = 0
    if (x + width - 25 == foe1_x and y == foe1_y) or ((x - width + 20) == foe1_x and y == foe1_y):
        danger = 1
        while hp != 0:
            if danger == 1 and hp != 0:
                hp -= 10
                break
    if damaging == True:
        if x >= (foe1_x - 20) and x <= (foe1_x + 20) and y == foe1_y and foe1_hp > 0:
            foe1_hp -= 1
    elif foe1_hp <= 0:
        foe1_y = 500
        foe1_dead = True
    elif foe1_hp > 0:
        foe1_y = 435
        foe1_dead = False



###
###Взаимодействие игрока с осязаемыми объектами
    falling = False
    fallCount = 5
    #if y != 140 and y != 435 and (x < (ob_x3 - 25) or x > (ob_x3 + 50)):
        #falling = True
    if falling == True and isJump == False:
        if y != 435:
            y += (fallCount ** 2)
            fallCount += 1
        else:
            falling = False
    if (y > 344 and y < 434) and (x > (ladderx - 20) and x < ladderx):
        if isJump == False:
            climbing = True
    elif (y > 344 and y < 434) and (x > (ladderx2 - 20) and x < ladderx2):
        if isJump == False:
            climbing = True
    else:
        climbing = False

    #if y > 435:
        #y = 435
    #elif jumpCount < 0:
    #elif (y < 340) and (x > (ob_x3 - 25) and x < (ob_x3 + 50)):
        #if y != 340:
            #y += (fallCount ** 2)
        #elif y > 340:
            #y = 340
        #fallCount += 1
    #elif (y == 340) and (x > (ob_x3 - 25) and x < (ob_x3 + 50)):



        #jumpCount = 10
        #isJump = False
        #falling = False
    #pygame.draw.rect(win, (255, 200, 0), (ob_x3, 400, 70, 20))

#(ob_x3, 400, 70, 20))

###



###Стрелы
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
###

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if x > (ladderx - 20) and x < ladderx:
            if y >= 345 and y <= 435:
                y -= 2
                climbing = True
                #x = (ladderx - 30)
        if x > (ladderx2 - 20) and x < ladderx2:
            if y >= 345 and y <= 435:
                y -= 2
                climbing = True
    if keys[pygame.K_s]:
        if x > (ladderx - 20) and x < ladderx:
            if y > 320 and y < 435:
                y += 2
                climbing = True
                #x = (ladderx - 20)
        if x > (ladderx2 - 20) and x < ladderx2:
            if y > 320 and y < 435:
                y += 2
                climbing = True


    if keys[pygame.K_c]:

        if (x > (ob_x - 20) and x < (ob_x +50)) and y == 435:
            y = 140
        #if x > (wallx + 1400) and x > (wallx + 1450):


    if keys[pygame.K_v ]:
        if (x > (ob_x - 20) and x < (ob_x +50)) and y == 140:
            y = 435
    if keys[pygame.K_h] and moving == False:
        attacking = True
        if x >= (foe_x - 20) and x <= (foe_x + 20) and y == foe_y and foe_hp > 0:
            foe_hp -= 1
            damaging = True
    else:
        attacking = False
        damaging = False


    if keys[pygame.K_l]:
        if hp > 0:
            hp -= 5
    if keys[pygame.K_o]:
        if (hp < 100 and death == 0):
            hp += 5
        elif foe_hp < 10:
            foe_hp += 1
    if keys[pygame.K_f]:
        if lastMove == "right":
            facing = 1
        else:
            facing = -1
        if len(bullets) < 5:
            bullets.append(arrow(round(x + width // 2), round(y +
            height // 2), 5, (255, 0, 0), facing))

    if keys[pygame.K_a] and x > 10 and x_level > 10 and climbing == False:
        moving = True
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
            #ob_x3 += speed
            ob_x4 += speed
            ob_x5 += speed
            wallx += speed
            ladderx += speed
            ladderx2 += speed
            archer_x += speed
            if foe_hp <= 0:
                foe_x += speed
            if infov1 == False:
                foe1_x += speed



    elif keys[pygame.K_d] and (x < 500 - width - 10) and (x_level < 2000 - width - 10) and climbing == False:
        moving = True
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
            #ob_x3 -= speed
            ob_x4 -= speed
            ob_x5 -= speed
            wallx -= speed
            ladderx -= speed
            ladderx2 -= speed
            archer_x -= speed
            if foe_hp <= 0:
                foe_x -= speed
            if infov1 == False:
                foe1_x -= speed

    else:
        left = False
        right = False
        animCount = 0
        moving = False
    #landing = True

    if not(isJump):
        if (keys[pygame.K_SPACE]) and jumpNo == False:
            isJump = True
    else:
        if jumpCount >= -10:# jumpCount 10 - игрок начал прыжок, 0 - середина прыжка - 10 - закончил прыжок
            if jumpCount < 0:#Игрок падает вниз
                y += (jumpCount ** 2) / 6
                #falling = True
                #isJump = False
                #jumpCount = 10
            else:
                y -= (jumpCount ** 2) / 6
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    drawWindow()


pygame.quit()
