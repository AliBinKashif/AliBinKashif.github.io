# coding: utf-8
def addFruit(screen):
    import random
    x = random.randint(154, 892)
    y = random.randint(154, 892)
    center = pygame.Vector2((x, y))
    pygame.draw.circle(screen, "red", center, 4)
    return center

def InitialiseSnake(screen):
    while len(Snake) != 4:
        Snake.pop(4)
    Snake[0] = pygame.Rect(500, 500, 10, 10)
    Snake[1] = pygame.Rect(500, 510, 10, 10)
    Snake[2] = pygame.Rect(500, 520, 10, 10)
    Snake[3] = pygame.Rect(500, 530, 10, 10)
    for i in range(4):
        pygame.draw.rect(screen, "green", Snake[i])

def MoveSnake(screen, Compass):
    for i in range (len(Snake)-1,0,-1):
        Snake[i] = Snake[i-1].copy()
        pygame.draw.rect(screen, "green", Snake[i])
    keys = pygame.key.get_pressed()
    if Compass == 0:
        if keys[pygame.K_d]:
            Snake[0].x += 10
            Compass = 1
        elif keys[pygame.K_a]:
            Snake[0].x -= 10
            Compass = 3
        else:
            Snake[0].y -= 10
    elif Compass == 1:
        if keys[pygame.K_w]:
            Snake[0].y -= 10
            Compass = 0
        elif keys[pygame.K_s]:
            Snake[0].y += 10
            Compass = 2
        else:
            Snake[0].x += 10
    elif Compass == 2:
        if keys[pygame.K_d]:
            Snake[0].x += 10
            Compass = 1
        elif keys[pygame.K_a]:
            Snake[0].x -= 10
            Compass = 3
        else:
            Snake[0].y += 10           
    elif Compass == 3:
        if keys[pygame.K_w]:
            Snake[0].y -= 10
            Compass = 0
        elif keys[pygame.K_s]:
            Snake[0].y += 10
            Compass = 2
        else:
            Snake[0].x -= 10


    pygame.draw.rect(screen, "green", Snake[0])
    return Compass




def DetectCollision(screen, Compass, center, score):
    import math
    changePos = False
    x1 = center.x
    x2 = Snake[0].x
    y1 = center.y
    y2 = Snake[0].y
    distance = math.sqrt((x2-x1)**2 + (y1-y2)**2)
    if Compass == 0:
        if distance <= 6.4:
            changePos = True
    elif Compass == 1:
        if distance <= 10.7:
            changePos = True
    elif Compass == 2:
        if distance <= 10.7:
            changePos = True
    elif Compass == 3:
        if distance <= 6.4:
            changePos = True

    if changePos:
        EnlargeSnake(screen, Compass)
        return addFruit(screen), score + 10
    else:
        pygame.draw.circle(screen, "red", center, 4)
        return center, score




def StartScreen(screen, running):
    screen.fill("black")
    font1 = pygame.font.SysFont("Arial", 32)
    text_render1 = font1.render("SNAKE GAME", True, "white")
    text_rect1 = text_render1.get_rect()
    text_rect1.center = (960, 600)
    font2 = pygame.font.SysFont("Arial", 20)
    text_render2 = font2.render("press any key to start", True, "white")
    text_rect2 = text_render2.get_rect()
    text_rect2.center = (960, 675)
    screen.blit(text_render1, text_rect1)
    screen.blit(text_render2, text_rect2)
    pygame.display.flip()
    waiting = True
    while waiting and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                waiting = False
    return running





def DetectWall(screen, Compass, running, score):
    if Compass == 0:
        if Snake[0].y == 150:
            running, score = EndScreen(screen, running, score)
    elif Compass == 1:
        if Snake[0].x == 890:
            running, score = EndScreen(screen, running, score)
    elif Compass == 2:
        if Snake[0].y == 890:
            running, score = EndScreen(screen, running, score)
    elif Compass == 3:
        if Snake[0].x == 150:
            running, score = EndScreen(screen, running, score)
    return running, score



def EndScreen(screen, running, score):
    screen.fill("black")

    font1 = pygame.font.SysFont("Arial", 32)
    text_render1 = font1.render("GAME OVER", True, "white")
    text_rect1 = text_render1.get_rect()
    text_rect1.center = (960, 600)

    font2 = pygame.font.SysFont("Arial", 20)
    text_render2 = font2.render("press any key to start", True, "white")
    text_rect2 = text_render2.get_rect()
    text_rect2.center = (960, 675)

    font3 = pygame.font.SysFont("Arial", 20)
    text_render3 = font3.render("Score: "+str(score), True, "white")
    text_rect3 = text_render3.get_rect()
    text_rect3.center = (960, 715)

    screen.blit(text_render1, text_rect1)
    screen.blit(text_render2, text_rect2)
    screen.blit(text_render3, text_rect3)
    pygame.display.flip()

    waiting = True
    while waiting and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = StartScreen(screen, running)
                InitialiseSnake(screen)
                waiting = False
    return running, 10




def EnlargeSnake(screen, Compass):
    lastX = Snake[len(Snake)-1].x
    lastY = Snake[len(Snake)-1].x
    secondLastX = Snake[len(Snake)-2].x
    secondLastY = Snake[len(Snake)-2].y
    if lastX - secondLastX < -7:
        Snake.append(pygame.Rect(lastX-10, lastY, 10, 10))
    elif lastX - secondLastX > 7:
        Snake.append(pygame.Rect(lastX+10, lastY, 10, 10))
    elif lastY - secondLastY < -7:
        Snake.append(pygame.Rect(lastX,lastY-10, 10, 10 ))
    elif lastY - secondLastY > 7:
        Snake.append(pygame.Rect(lastX, lastY+10, 10, 10 ))




def CheckForCollision(screen, running, score):
    for i in range(1, len(Snake)):
        if Snake[0].colliderect(Snake[i]):
            running, score = EndScreen(screen, running, score)
            break
    return running, score




def ScoreBoard(screen, score):
    font = pygame.font.SysFont("Arial", 32)
    renderer = font.render("score:"+str(score), True, "white")
    rect = renderer.get_rect()
    rect.center = (1500, 300)
    screen.blit(renderer, rect)








import pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1200))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
running = True
start = True
Snake = [0 for i in range(4)]
score = 10
Compass = 0
running = StartScreen(screen, running)
InitialiseSnake(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("black")

    outerSquare = pygame.Rect(100, 100, 850, 850)
    pygame.draw.rect(screen, "purple", outerSquare)
    innerSquare = pygame.Rect(150, 150, 750, 750)
    pygame.draw.rect(screen, "black", innerSquare)
    Compass = MoveSnake(screen, Compass)
    ScoreBoard(screen, score)
    if start:
        center = addFruit(screen)
        start = False
    else:
        center, score = DetectCollision(screen, Compass, center, score)
        running, score = DetectWall(screen, Compass, running, score)
        running, score = CheckForCollision(screen, running, score)
    pygame.time.delay(50)
    clock.tick(60)
    pygame.display.flip()


pygame.quit()
