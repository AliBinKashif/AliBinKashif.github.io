# coding: utf-8
import pygame
import random




def DefineSlabPosition():
    slab[0] = pygame.Rect(0, 1065, 200, 50)
    slab[1] = pygame.Rect(320, 1015, 50, 50)
    slab[2] = pygame.Rect(600, 1085, 50, 50)
    slab[3] = pygame.Rect(700, 1065, 50, 50)
    slab[4] = pygame.Rect(980, 1085, 50, 50)
    slab[5] = pygame.Rect(1160, 1055, 50, 50)
    slab[6] = pygame.Rect(1300, 1085, 50, 50)
    slab[7] = pygame.Rect(1580, 1015, 50, 50)
    slab[8] = pygame.Rect(1760, 1035, 50, 50)
    slab[9] = pygame.Rect(1870, 935, 50, 50)
    slab[10] = pygame.Rect(0, 785, 1800, 50)
    slab[11] = pygame.Rect(0, 625, 100, 50)
    slab[12] = pygame.Rect(130, 480, 1920-130, 50)
    slab[13] = pygame.Rect(0, 180, 1920, 50)


def InVoid(ninjaPosX, ninjaPosY, currentSlab, respawnX, respawnY, respawnSlab, health):
    if ninjaPosY > 1100:
        ninjaPosX = respawnX
        ninjaPosY = respawnY
        currentSlab = respawnSlab
        health = 100
    return ninjaPosX, ninjaPosY, currentSlab, health




def DetectSlab(currentSlab, ninjaRect):
    if  currentSlab < 12 and ninjaRect.colliderect(slab[currentSlab+1]):
        currentSlab+=1
    elif currentSlab > 0 and ninjaRect.colliderect(slab[currentSlab-1]):
        currentSlab-=1
    return currentSlab




def MoveSlab3and6(forward):
    if forward:
        slab[3].x+=5
        slab[6].x+=5
    else:
        slab[3].x-=5
        slab[6].x-=5

    if slab[3].x == 700:
        forward = True
    elif slab[3].x == 900:
        forward = False

    return forward




def CheckPoint(currentSlab, respawnX, respawnY, respawnSlab):
    if currentSlab == 9:
        respawnX = 1880
        respawnY = 870
        respawnSlab = 9
    elif currentSlab == 11:
        respawnX = 10
        respawnY = 555
        respawnSlab = 11
    return respawnX, respawnY, respawnSlab




def DisplayThorns(screen):
    thorn = "Thornny.png"
    thornsHitBox[0] = pygame.Rect(1680, 735, 50, 50)
    thornsImage[0] = pygame.image.load(thorn).convert()
    thornsHitBox[1] = pygame.Rect(1550, 735, 50, 50)
    thornsImage[1] = pygame.image.load(thorn).convert()
    thornsHitBox[2] = pygame.Rect(1420, 535, 50, 50)
    thornsImage[2] = pygame.image.load(thorn).convert()
    thornsHitBox[3] = pygame.Rect(1320, 735, 50, 50)
    thornsImage[3] = pygame.image.load(thorn).convert()
    thornsHitBox[4] = pygame.Rect(1170, 735, 50, 50)
    thornsImage[4] = pygame.image.load(thorn).convert()
    thornsHitBox[5] = pygame.Rect(1120, 735, 50, 50)
    thornsImage[5] = pygame.image.load(thorn).convert()
    thornsHitBox[6] = pygame.Rect(1050, 535, 50, 50)
    thornsImage[6] = pygame.image.load(thorn).convert()
    thornsHitBox[7] = pygame.Rect(950, 735, 50, 50)
    thornsImage[7] = pygame.image.load(thorn).convert()

    for i in range(8):
        screen.blit(thornsImage[i], (thornsHitBox[i].x, thornsHitBox[i].y))




def OnCollisionWithThorn(ninjaPosX, right, ninjaRect, health):
    for i in range(8):
        if ninjaRect.colliderect(thornsHitBox[i]):
            health-=2
            if right:
                ninjaPosX = thornsHitBox[i].x-32
            else:
                ninjaPosX = thornsHitBox[i].x+50
            break
    return ninjaPosX, health




def CheckHealth(ninjaPosX, ninjaPosY, currentSlab, respawnX, respawnY, respawnSlab, health):
    if health <= 0:
        ninjaPosX = respawnX
        ninjaPosY = respawnY
        currentSlab = respawnSlab
        health = 100
    return ninjaPosX, ninjaPosY, currentSlab, health




def DisplayHealthBar(ninjaPosX, ninjaPosY, health, screen):
    redBar = pygame.Rect(ninjaPosX-9, ninjaPosY-10, 50, 5)
    greenBar = pygame.Rect(ninjaPosX-9, ninjaPosY-10, health/2, 5)
    pygame.draw.rect(screen, "red", redBar)
    pygame.draw.rect(screen, "green", greenBar)




def ShoorArrow(screen, arrowPosX):
    arrowShooter = pygame.image.load("ArrowShooter.png").convert()
    screen.blit(arrowShooter, (0,735))
    arrow = pygame.image.load("Arrow.png").convert()
    arrowRect = pygame.Rect(arrowPosX, 757, 50, 6)
    screen.blit(arrow, (arrowPosX, 757))
    arrowPosX+=10
    if arrowPosX == 900:
        arrowPosX = 50
    return arrowPosX, arrowRect




def CheckForCollisionWithArrow(arrowRect, ninjaRect, health, arrowPosX):
    if arrowRect.colliderect(ninjaRect):
        health-=8
        arrowPosX = 50
        #without this code, there would be problems with the health bar display
        if health < 0:
            health = 0
    return health, arrowPosX




def AddFire(screen, toggle):
    fireImage = "Fire.png"
    for i in range(15):
        fire[i] = pygame.image.load(fireImage).convert()
    if toggle <= 23:
        screen.blit(fire[0], (230, 330))
        fireHitBox[0] = pygame.Rect(230, 330, 50, 150)
    elif toggle <= 47:
        screen.blit(fire[1], (280, 330))
        fireHitBox[1] = pygame.Rect(280, 330, 50, 150)
    elif toggle <= 71:
        screen.blit(fire[2], (330, 330))
        fireHitBox[2] = pygame.Rect(330, 330, 50, 150)

    if toggle <= 35:
        screen.blit(fire[3], (450, 330))
        fireHitBox[3] = pygame.Rect(450, 330, 50, 150)
        screen.blit(fire[5], (550, 330))
        fireHitBox[5] = pygame.Rect(550, 330, 50, 150)
    elif toggle <= 71:
        screen.blit(fire[4], (500, 330))
        fireHitBox[4] = pygame.Rect(500, 330, 50, 150)
        screen.blit(fire[6], (600, 330))
        fireHitBox[6] = pygame.Rect(600, 330, 50, 150)

    if toggle <= 11:
        screen.blit(fire[7], (750, 330))
        fireHitBox[7] = pygame.Rect(600, 330, 50, 150)
    elif toggle <= 23:
        screen.blit(fire[8], (800, 330))
        fireHitBox[8] = pygame.Rect(800, 330, 50, 150)
    elif toggle <= 35:
        screen.blit(fire[9], (850, 330))
        fireHitBox[9] = pygame.Rect(850, 330, 50, 150)
    elif toggle <= 47:
        screen.blit(fire[10], (900, 330))
        fireHitBox[10] = pygame.Rect(900, 330, 50, 150)
    elif toggle <= 59:
        screen.blit(fire[10], (950, 330))
        fireHitBox[10] = pygame.Rect(950, 330, 50, 150)
    elif toggle <= 71:
        screen.blit(fire[10], (1000, 330))
        fireHitBox[10] = pygame.Rect(1000, 330, 50, 150)

    if toggle <= 17:
        screen.blit(fire[11], (1100, 330))
        fireHitBox[11] = pygame.Rect(1100, 330, 50, 150)
    elif toggle <= 35:
        screen.blit(fire[12], (1200, 330))
        fireHitBox[12] = pygame.Rect(1200, 330, 50, 150)
    elif toggle <= 47:
        screen.blit(fire[13], (1300, 330))
        fireHitBox[13] = pygame.Rect(1300, 330, 50, 150)
    elif toggle <= 71:
        screen.blit(fire[14], (1400, 330))
        fireHitBox[14] = pygame.Rect(1400, 330, 50, 150)    
    toggle= (toggle+1)%72    
    return toggle   




def CheckForCollisionWithFire(ninjaRect, health):
    for i in range(11):
        if fireHitBox[i] != 0 and ninjaRect.colliderect(fireHitBox[i]):
            health-=4
            #prevents error in displaying health bar
            if health < 0:
                health = 0
            break
    return health





def VictoryScreen(screen, ninjaPosX, running):
    if currentSlab == 12 and ninjaPosX > 1500:
        screen.fill("black")
        font = pygame.font.SysFont("Arial", 32)
        renderer = font.render("GAME OVER", True, "white")
        textRect = renderer.get_rect()
        textRect.center = (960, 600)
        screen.blit(renderer, textRect)
        pygame.display.flip()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
    return running



pygame.init()
screen = pygame.display.set_mode((1920, 1200))
clock = pygame.time.Clock()
pygame.display.set_caption("Ninja game")
running = True
right = True
ninjaPos = ["ningaLeft.png", "ningaRight.png"]
ninjaPosX = 10
ninjaPosY = 1000
ninjaRect = pygame.Rect(ninjaPosX, ninjaPosY, 32, 64)
slab = [0]*20
thornsHitBox = [0]*10
thornsImage = [0]*10
fire = [0]*15
fireHitBox = [0]*15
DefineSlabPosition()
currentSlab = 0
health = 100
#tells if slab3and6 is moving forward or backwards
forward = True
respawnX = 10
respawnY = 1000
#tells horizontal position of arrows
arrowPosX = 50
respawnSlab = 0
#helps us to make a pattern in the first three fires
firstThreeToggle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            for i in range(13):
                if ninjaRect.colliderect(slab[i]):       
                    if keys[pygame.K_UP] or keys[pygame.K_w]:
                        ninjaPosY-=100
    screen.fill((99, 3, 48))
    ninja = pygame.image.load(ninjaPos[right]).convert()
    screen.blit(ninja, (ninjaPosX, ninjaPosY))
    ninjaRect = pygame.Rect(ninjaPosX, ninjaPosY, 32, 64)
    currentSlab = DetectSlab(currentSlab, ninjaRect)
    forward = MoveSlab3and6(forward)
    arrowPosX, arrowRect = ShoorArrow(screen, arrowPosX)
    respawnX, respawnY, respawnSlab = CheckPoint(currentSlab, respawnX, respawnY, respawnSlab)
    DisplayThorns(screen)
    health, arrowPosX = CheckForCollisionWithArrow(arrowRect, ninjaRect, health, arrowPosX)
    ninjaPosX, health = OnCollisionWithThorn(ninjaPosX, right, ninjaRect, health)
    DisplayHealthBar(ninjaPosX, ninjaPosY, health, screen)
    firstThreeToggle = AddFire(screen, firstThreeToggle)
    health = CheckForCollisionWithFire(ninjaRect, health)
    for i in range(15):
        fireHitBox[i] = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        right = True
        ninjaPosX+=10
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        right = False
        ninjaPosX-=10
    for i in range(14):
        pygame.draw.rect(screen, "azure4", slab[i])
    pygame.draw.rect(screen, "bisque4", slab[currentSlab])
    if not(ninjaRect.colliderect(slab[currentSlab])) or ninjaRect.y+48 > slab[currentSlab].y:
        ninjaPosY += 10
    ninjaPosX, ninjaPosY, currentSlab, health = InVoid(ninjaPosX, ninjaPosY, currentSlab, respawnX, respawnY, respawnSlab, health)
    ninjaPosX, ninjaPosY, currentSlab, health = CheckHealth(ninjaPosX, ninjaPosY, currentSlab, respawnX, respawnY, respawnSlab, health)
    running = VictoryScreen(screen, ninjaPosX, running)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
