# coding: utf-8
import pygame




def DislpayBoard(board, numberOnBoard, screen):
    font = pygame.font.SysFont("Arial", 64)
    for i in range(4):
        for j in range(4):
            if numberOnBoard[i][j] == 0:
                color = "white"
            elif numberOnBoard[i][j] == 2:
                color = "antiquewhite"
            elif numberOnBoard[i][j] == 4:
                color = "antiquewhite3"
            elif numberOnBoard[i][j] == 8:
                color = "antiquewhite4"
            elif numberOnBoard[i][j] == 16:
                color = "brown"
            elif numberOnBoard[i][j] == 32:
                color = "brown2"
            elif numberOnBoard[i][j] == 64:
                color = "brown3"
            elif numberOnBoard[i][j] == 128:
                color = "brown4"
            elif numberOnBoard[i][j] == 256:
                color = "purple1"
            elif numberOnBoard[i][j] == 512:
                color = "purple3"
            elif numberOnBoard[i][j] == 1024:
                color = "purple4"
            elif numberOnBoard[i][j] == 2048:
                color = "black"
            pygame.draw.rect(screen, color, board[i][j])
            if numberOnBoard[i][j] != 0:
                renderer = font.render(str(numberOnBoard[i][j]), True, "orange4")
                fontrect = renderer.get_rect()
                fontrect.center = (board[i][j].x+50, board[i][j].y+50)
                screen.blit(renderer, fontrect)




def Up(numberOnBoard, filled, score):
    for i in range(1, 4):
        for j in range(4):
            move = True
            currentPos = i
            while move:
                if currentPos == 0 or numberOnBoard[currentPos-1][j] != 0:
                    move = False
                else:
                    numberOnBoard[currentPos-1][j] = numberOnBoard[currentPos][j]
                    numberOnBoard[currentPos][j] = 0
                    currentPos-=1
                if currentPos != 0 and numberOnBoard[currentPos][j] == numberOnBoard[currentPos-1][j]:
                    numberOnBoard[currentPos][j] = 0
                    numberOnBoard[currentPos-1][j]*=2
                    if numberOnBoard[currentPos-1][j] != 0:
                        filled-=1
                        score+=numberOnBoard[currentPos-1][j]
    return filled, score




def Down(numberOnBoard, filled, score):
    for i in range(2, -1, -1):
        for j in range(4):
            move = True
            currentPos = i
            while move:
                if currentPos == 3 or numberOnBoard[currentPos+1][j] != 0:
                    move = False
                else:
                    numberOnBoard[currentPos+1][j] = numberOnBoard[currentPos][j]
                    numberOnBoard[currentPos][j] = 0
                    currentPos+=1
                if currentPos != 3 and numberOnBoard[currentPos][j] == numberOnBoard[currentPos+1][j]:
                    numberOnBoard[currentPos][j] = 0
                    numberOnBoard[currentPos+1][j]*=2          
                    if numberOnBoard[currentPos+1][j] != 0:
                        filled-=1
                        score+=numberOnBoard[currentPos+1][j]
    return filled, score




def Right(numberOnBoard, filled, score):
    for j in range(2,-1,-1):
        for i in range(4):
            move = True
            currentPos = j
            while move:
                if currentPos == 3 or numberOnBoard[i][currentPos+1] != 0:
                    move = False
                else:
                    numberOnBoard[i][currentPos+1] = numberOnBoard[i][currentPos]
                    numberOnBoard[i][currentPos] = 0
                    currentPos+=1
                if currentPos != 3 and numberOnBoard[i][currentPos] == numberOnBoard[i][currentPos+1]:
                    numberOnBoard[i][currentPos] = 0
                    numberOnBoard[i][currentPos+1]*=2
                    if numberOnBoard[i][currentPos+1] != 0:           
                        filled-=1
                        score+=numberOnBoard[i][currentPos+1]
    return filled, score




def Left(numberOnBoard, filled, score):
    for j in range(1,4):
        for i in range(4):
            move = True
            currentPos = j
            while move:
                if currentPos == 0 or numberOnBoard[i][currentPos-1] != 0:
                    move = False
                else:
                    numberOnBoard[i][currentPos-1] = numberOnBoard[i][currentPos] 
                    numberOnBoard[i][currentPos] = 0
                    currentPos-=1
                if currentPos != 0 and numberOnBoard[i][currentPos] == numberOnBoard[i][currentPos-1]:
                    numberOnBoard[i][currentPos] = 0
                    numberOnBoard[i][currentPos-1]*=2         
                    if numberOnBoard[i][currentPos-1] != 0: 
                        filled-=1
                        score+=numberOnBoard[i][currentPos-1]
    return filled, score




def Add(numberOnBoard, filled):
    import random
    if filled != 16:
        y = random.randint(0, 3)
        x = random.randint(0, 3)
        while numberOnBoard[y][x] != 0:
            y = random.randint(0, 3)
            x = random.randint(0, 3)
        numberOnBoard[y][x] = 2
        filled += 1
    return filled          




def CheckLoss(filled, numberOnBoard, screen, running):
    loss = False
    if filled == 16:
        loss = True
        for i in range(3):
            for j in range(3):
                if numberOnBoard[i][j] == numberOnBoard[i][j+1] or numberOnBoard[i][j] == numberOnBoard[i+1][j]:
                    loss = False
                    break
    if loss:
        running, filled = LossScreen(screen, running, filled)
    return running, filled




def CheckVictory(numberOnBoard, running, filled):
    for i in range(4):
        for j in range(4):
            if numberOnBoard[i][j] == 2048:
                running, filled = VicoryScreen(screen, running, filled)
                break
    return running, filled





def LossScreen(screen, running, filled):
    screen.fill("black")
    font1 = pygame.font.SysFont("Arial", 64)
    renderer1 = font1.render("GameOver", True, "white")
    rect1 = renderer1.get_rect()
    rect1.center = (960, 450)
    screen.blit(renderer1, rect1)

    font2 = pygame.font.SysFont("Arial", 20)
    renderer2 = font2.render("press any key to continue", True, "white")
    rect2 = renderer2.get_rect()
    rect2.center = (960, 650)
    screen.blit(renderer2, rect2)
    pygame.display.flip()    

    paused = True
    while running and paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = StartScreen(screen, running)
                for i in range(4):
                    for j in range(4):
                        numberOnBoard[i][j] = 0
                numberOnBoard[3][3] = 2
                numberOnBoard[2][1] = 2
                filled = 2
                paused = False
    return running, filled




def VictoryScreen(screen, running, filled):
    screen.fill("black")
    font1 = pygame.font.SysFont("Arial", 64)
    renderer1 = font1.render("You Won", True, "white")
    rect1 = renderer1.get_rect()
    rect1.center = (960, 450)
    screen.blit(renderer1, rect1)

    font2 = pygame.font.SysFont("Arial", 20)
    renderer2 = font2.render("press any key to continue", True, "white")
    rect2 = renderer2.get_rect()
    rect2.center = (960, 650)
    screen.blit(renderer2, rect2)
    pygame.display.flip()

    paused = True
    while running and paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = StartScreen(screen, running)
                for i in range(4):
                    for j in range(4):
                        numberOnBoard[i][j] = 0
                numberOnBoard[3][3] = 2
                numberOnBoard[2][1] = 2
                filled = 2
                paused = False
    return running, filled





def StartScreen(screen, running):
    screen.fill("black")   
    font1 = pygame.font.SysFont("Arial", 64)
    renderer1 = font1.render("2048", True, "white")
    rect1 = renderer1.get_rect()
    rect1.center = (960, 450)
    screen.blit(renderer1, rect1)

    font2 = pygame.font.SysFont("Arial", 20)
    renderer2 = font2.render("press any to start", True, "white")
    rect2 = renderer2.get_rect()
    rect2.center = (960, 650)
    screen.blit(renderer2, rect2)
    pygame.display.flip()

    paused = True
    while running and paused:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            paused = False
    return running
pygame.init()
screen = pygame.display.set_mode((1920, 1200))
pygame.display.set_caption("2048")
clock = pygame.time.Clock()
gameRect = pygame.Rect(710, 350, 500, 500)
board = [[0 for i in range(4)] for j in range(4)]
x = 730
y = 370
for i in range(4):
    for j in range(4):
        board[i][j] = pygame.Rect(x, y, 100, 100)
        x+=120
        if j == 3:
            x = 730
    y+=120

numberOnBoard = [[0]*4  for j in range(4)]
numberOnBoard[3][3] = 2
numberOnBoard[2][1] = 2
running = True
filled = 2
score = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                filled, score = Up(numberOnBoard, filled, score)
                filled = Add(numberOnBoard, filled)
            elif keys[pygame.K_DOWN]:
                filled, score = Down(numberOnBoard, filled, score)
                filled = Add(numberOnBoard, filled)
            elif keys[pygame.K_RIGHT]:
                filled, score = Right(numberOnBoard, filled, score)
                filled = Add(numberOnBoard, filled)
            elif keys[pygame.K_LEFT]:
                filled, score = Left(numberOnBoard, filled, score)
                filled = Add(numberOnBoard, filled)
    screen.fill("black")
    pygame.draw.rect(screen, "bisque4", gameRect)
    DislpayBoard(board, numberOnBoard, screen)
    font = pygame.font.SysFont("Arial", 40)
    renderer = font.render("score:"+str(score), True, "white")
    rect = renderer.get_rect()
    rect.center = (970, 300)
    screen.blit(renderer, rect)
    running, filled = CheckLoss(filled, numberOnBoard, screen, running)
    running, filled = CheckVictory(numberOnBoard, running, filled)
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
