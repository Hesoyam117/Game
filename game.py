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

clock = pygame.time.Clock()

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
levelCount = 0

left = False
right = False
animCount = 0
lastMove = "right"
foe_left = True
foe_right = False
foe_animCount = 0

foe_x = 400
foe_y = 435
foe_speed = 3


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
    if levelCount == 0:
        win.blit(bg, (0, 0))
    if levelCount == 1:
        win.blit(bg2, (0, 0))

    win.blit(hp_bar, (20, 20))
    pygame.draw.rect(win, (255, 0, 0), (23, 23, hp, 30))
    #win.blit(arab, (foe_x, foe_y))
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
    if hp <= 0:
        death = 1
        win.blit(dead_scr, (0, 0))


    pygame.display.update()

run = True
bullets = []
arabs = []
while run:
    clock.tick(30)
    if ((x + width - 25) <= foe_x and y >= foe_y):
        foe_x -= foe_speed
        foe_left = True
        foe_right = False
    elif ((x - width + 25) >= foe_x):
        foe_x += foe_speed
        foe_right = True
        foe_left = False
    if (((x + width - 25) == foe_x) or ((x - width + 25) == foe_x) and y >= foe_y):
        #time.sleep
        if (hp != 0):
            hp -= 5
            #time.sleep(5)
    #if x > 425:
        #levelCount += 1
        #x == 50
        #win.blit(bg2, (0, 0))
    #elif (x < 45) and (levelCount > 0):
        #levelCount -= 1
        #x == 479

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

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

    if keys[pygame.K_a] and x > 10:
        x -= speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_d] and x < 500 - width - 10:
        x += speed
        left = False
        right = True
        lastMove = "right"
    else:
        left = False
        right = False
        animCount = 0

    if not(isJump):
        if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10
    drawWindow()


pygame.quit()
