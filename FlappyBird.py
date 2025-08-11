# coding: utf-8
import pygame



def TouchGround(birdPosX, birdPosY,  screen, running, score, currentPillar):
    if birdPosY > 1168:
        running = EndScreen(screen, running, score)
        birdPosX = 153
        birdPosY = 600
        score = 0
        currentPillar = 0
    return running, birdPosX, birdPosY, score, currentPillar




def EndScreen(screen, running, score):
    screen.fill("black")

    font1 = pygame.font.SysFont("Arial", 32)
    text_render1 = font1.render("GAME OVER", True, "white")
    text_rect1 = text_render1.get_rect()
    text_rect1.center = (960, 600)
    screen.blit(text_render1, text_rect1)

    font2 = pygame.font.SysFont("Arial", 20)
    text_renderer2 = font2.render("press ENTER to enter to continue", True, "white")
    text_rect2 = text_renderer2.get_rect()
    text_rect2.center = (960, 675)
    screen.blit(text_renderer2, text_rect2)

    font3 = pygame.font.SysFont("Arial", 20)
    text_renderer3 = font3.render("Score: "+str(score), True, "white")
    text_rect3 = text_renderer3.get_rect()
    text_rect3.center = (960, 715)
    screen.blit(text_renderer3, text_rect3)

    pygame.display.flip()

    waiting = True
    while waiting and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    running = StartScreen(screen, running)
                    waiting = False

    return running




def StartScreen(screen, running):
    screen.fill("black")

    font1 = pygame.font.SysFont("Arial", 32)
    text_renderer1 = font1.render("Flappy Bird", True, "white")
    text_rect1 = text_renderer1.get_rect()
    text_rect1.center = (960, 600)
    screen.blit(text_renderer1, text_rect1)

    font2 = pygame.font.SysFont("Arial", 20)
    text_renderer2 = font2.render("press ENTER to start", True, "white")
    text_rect2 = text_renderer2.get_rect()
    text_rect2.center = (960, 700)
    screen.blit(text_renderer2, text_rect2)

    pygame.display.flip()

    waiting = True
    while waiting and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RETURN]:
                    waiting = False

    return running




def InitialisePillars():
    pillarUpper[0]  = pygame.Rect(481, 0, 160, 300)
    pillarBottom[0] = pygame.Rect(481, 429+64+64, 160, 708-64)
    pillarUpper[1] = pygame.Rect(481+560, 0, 160, 100)
    pillarBottom[1] = pygame.Rect(481+560, 293+64, 160, 908-64)
    pillarUpper[2] = pygame.Rect(481+560*2, 0, 160, 700)
    pillarBottom[2] = pygame.Rect(481+560*2, 893+64, 160, 308-64)
    pillarUpper[3] = pygame.Rect(481+560*3, 0, 160, 400)
    pillarBottom[3] = pygame.Rect(481+560*3, 593+64, 160, 608-64)
    pillarUpper[4] = pygame.Rect(481+560*4, 0, 160, 600)
    pillarBottom[4] = pygame.Rect(481+560*4, 793+64, 160, 508-64)
    pillarUpper[5] = pygame.Rect(481+560*5, 0, 160, 100)
    pillarBottom[5] = pygame.Rect(481+560*5, 293+64, 160, 908-64)
    pillarUpper[6] = pygame.Rect(481+560*6, 0, 160, 700)
    pillarBottom[6] = pygame.Rect(481+560*6, 893+64, 160, 308-64)
    pillarUpper[7] = pygame.Rect(481+560*7, 0, 160, 200)
    pillarBottom[7] = pygame.Rect(481+560*7, 393+64, 160, 808-64)
    pillarUpper[8] = pygame.Rect(481+560*8, 0, 160, 800)
    pillarBottom[8] = pygame.Rect(481+560*8, 993+64, 160, 208-64)
    pillarUpper[9] = pygame.Rect(481+560*9+100, 0, 160, 400)
    pillarBottom[9] = pygame.Rect(481+560*9+200, 593+64, 160, 608-64)


def DisplayPillars(screen):
    for i in range(10):
        pygame.draw.rect(screen, "purple", pillarUpper[i])
        pygame.draw.rect(screen, "purple", pillarBottom[i])




def MovePillars():
    for i in range(10):
        pillarUpper[i].x -= 4
        pillarBottom[i].x -=4
        if pillarUpper[i].x < -1920*2:
            pillarUpper[i].x = 1921
            pillarBottom[i].x = 1921




def TestForCollision(screen, running, score, imageHitBox, birdPosX, birdPosY, currentPillar):
    for i in range(10):
        if imageHitBox.colliderect(pillarUpper[i]) or imageHitBox.colliderect(pillarBottom[i]):
            running = EndScreen(screen, running, score)
            InitialisePillars()
            birdPosX = 153
            birdPosY = 600
            score = 0
            currentPillar = 0
    return running, birdPosX, birdPosY, score, currentPillar




def IncrementScore(currentPillar, birdPosX, score):
    if birdPosX + 64 > pillarUpper[currentPillar].x+160:
        currentPillar = (currentPillar+1)%10
        score+=10
    return currentPillar, score




def DisplayScore(screen, score):
    font = pygame.font.SysFont("Arial", 32)
    renderer = font.render("score:"+str(score), True, "white")
    text_rect = renderer.get_rect()
    text_rect.center = (1800, 50)
    screen.blit(renderer, text_rect)





pygame.init()
screen = pygame.display.set_mode((1920, 1200))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()
running = True
birdPosX = 153
birdPosY = 600
gravity = 10
jump = 25
score = 0
currentPillar = 0
running = StartScreen(screen, running)
pillarUpper = [0]*10
pillarBottom = [0]*10
InitialisePillars()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")
    DisplayPillars(screen)
    MovePillars()
    currentPillar, score = IncrementScore(currentPillar, birdPosX, score)
    bird = pygame.image.load("bird3.png").convert()
    screen.blit(bird, (birdPosX, birdPosY))
    DisplayScore(screen, score)
    imageHitBox = pygame.Rect(birdPosX, birdPosY, 64, 64)
    birdPosY += gravity
    running, birdPosX, birdPosY, score, currentPillar = TestForCollision(screen, running, score, imageHitBox, birdPosX, birdPosY, currentPillar)
    running, birdPosX, birdPosY, score, currentPillar = TouchGround(birdPosX, birdPosY, screen, running, score, currentPillar)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        birdPosY -= jump
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
