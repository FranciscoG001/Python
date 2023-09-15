import pygame
import random

def initVars():
    # Screen Size
    width = 640
    height = 720

    # Start Parameters
    start = False
    bird_x = (width/2)-20
    bird_y = height / 2
    countPoints = 0
    velBird = 0  
    gravity = 0.5
    pipePos_x = width
    pipePos_x2 = width * 2
    textColor = (255, 255, 255)

    # Star Pygame Loop
    running = True

    # Bird impulse
    impulse = -9

    # Pipes Velocity Move
    velocityPipeMove = 5

    # Start coords
    upPipPos_y = -370
    upPipPos_y2 = -270
    downPipPos_y = 520
    downPipPos_y2 = 620

    # To random pipes
    upPipPos_y_min = -250
    upPipPos_y_max = -550

    registPass = False
    registPass2 = False

    return registPass, registPass2, width,height,start,bird_x,bird_y,countPoints,velBird,gravity,pipePos_x,pipePos_x2,textColor,running,impulse,velocityPipeMove,upPipPos_y,upPipPos_y2,downPipPos_y,downPipPos_y2,upPipPos_y_min,upPipPos_y_max

def pygameSetup(width,height,countPoints,textColor):
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 100)
    displayText = font.render(str(countPoints), True, textColor)

    return screen,clock,font,displayText

def startGameParameters(width,height,font,textColor):
    start = True
    bird_x = (width/2)-20
    bird_y = height / 2
    velBird = 0  
    gravity = 0.5
    pipePos_x = width
    pipePos_x2 = width + 400
    countPoints = 0
    displayText = font.render(str(countPoints), True, textColor)
    return start,bird_x,bird_y,velBird,gravity,pipePos_x,pipePos_x2,countPoints,displayText

def countPoints(bird_x, pipePos_x, pipePos_x2, upPipeResizeImage, upPipeResizeImage2, registPass, registPass2, countPoints, displayText, font, textColor):
    if bird_x > pipePos_x + upPipeResizeImage.get_width() and not registPass:
        countPoints += 1
        displayText = font.render(str(countPoints), True, textColor)
        registPass = True
    elif bird_x <= pipePos_x + upPipeResizeImage.get_width():
        registPass = False
    if bird_x > pipePos_x2 + upPipeResizeImage2.get_width() and not registPass2:
        countPoints += 1
        displayText = font.render(str(countPoints), True, textColor)
        registPass2 = True
    elif bird_x <= pipePos_x2 + upPipeResizeImage2.get_width():
        registPass2 = False
    
    return countPoints, displayText, registPass, registPass2

def touchPipes(bird_x,bird_y,birdResizeImage,pipePos_x,pipePos_x2,upPipPos_y,upPipPos_y2,width,height,start):
    # Touch Pipes
    bird_rect = pygame.Rect(bird_x+13, bird_y+20, birdResizeImage.get_width()-23, birdResizeImage.get_height()-39)
    up_pipe_rect = pygame.Rect(pipePos_x, 0, width/7, upPipPos_y+720)
    down_pipe_rect = pygame.Rect(pipePos_x, upPipPos_y + 890, width/7, height)
    up_pipe_rect2 = pygame.Rect(pipePos_x2, 0, width/7, upPipPos_y2+720)
    down_pipe_rect2 = pygame.Rect(pipePos_x2, upPipPos_y2 + 890, width/7, height)

    # Pipes 1
    if bird_rect.colliderect(up_pipe_rect) or bird_rect.colliderect(down_pipe_rect):
        start = False
    # Pipes 2
    if bird_rect.colliderect(up_pipe_rect2) or bird_rect.colliderect(down_pipe_rect2):
        start = False
    
    return start

def groundOrSkyTouch(bird_y,start):
    if bird_y > 600:
        start = False
    if bird_y < 0:
        start = False
    return start

def startPageImages(screen,backgroundResizeImage,flappyBirdTextResizeImage,birdResizeImage,playButtonResizeImage,width,height):
    screen.blit(backgroundResizeImage,(0,0))
    screen.blit(flappyBirdTextResizeImage,(0,0))
    screen.blit(birdResizeImage,((width/2)-20,height/2))
    screen.blit(playButtonResizeImage,((width/2)-60,(height/2)-130))

def loadImages(width,height):
    # Load Images
    backgroundImage = pygame.image.load("Images/background.jpg")
    upPipeImage = pygame.image.load("Images/upPipe.png")
    downPipeImage = pygame.image.load("Images/downPipe.png")
    flappyBirdTextImage = pygame.image.load("Images/flappyBirdText.png")
    birdImage = pygame.image.load("Images/bird.png")
    playButtonImage = pygame.image.load("Images/playbtn.png")

    # Scale original image
    backgroundResizeImage = pygame.transform.scale(backgroundImage, (width, height))
    upPipeResizeImage = pygame.transform.scale(upPipeImage, (width/7, height))
    downPipeRisezeImage = pygame.transform.scale(downPipeImage, (width/7, height))
    upPipeResizeImage2 = pygame.transform.scale(upPipeImage, (width/7, height))
    downPipeRisezeImage2 = pygame.transform.scale(downPipeImage, (width/7, height))
    flappyBirdTextResizeImage = pygame.transform.scale(flappyBirdTextImage, (width, 200))
    birdResizeImage = pygame.transform.scale(birdImage, (75, 75))
    playButtonResizeImage = pygame.transform.scale(playButtonImage, (150, 75))

    # Convert to avoid the black pixeis of image
    birdResizeImage = birdResizeImage.convert_alpha()
    upPipeResizeImage = upPipeResizeImage.convert_alpha()
    downPipeRisezeImage = downPipeRisezeImage.convert_alpha()
    upPipeResizeImage2 = upPipeResizeImage2.convert_alpha()
    downPipeRisezeImage2 = downPipeRisezeImage2.convert_alpha()

    return backgroundResizeImage, upPipeResizeImage, downPipeRisezeImage, upPipeResizeImage2, downPipeRisezeImage2, flappyBirdTextResizeImage, birdResizeImage, playButtonResizeImage

def resetPipes(pipePos_x,pipePos_x2,upPipeResizeImage,upPipeResizeImage2,upPipPos_y_max,upPipPos_y_min,width,upPipPos_y,upPipPos_y2,downPipPos_y,downPipPos_y2):
    if pipePos_x + upPipeResizeImage.get_width() < -50:
            upPipPos_y = random.randint(upPipPos_y_max,upPipPos_y_min) # New position
            downPipPos_y = upPipPos_y + 890
            pipePos_x = width
    if pipePos_x2 + upPipeResizeImage2.get_width() < -50:
        upPipPos_y2 = random.randint(upPipPos_y_max,upPipPos_y_min) # New position
        downPipPos_y2 = upPipPos_y2 + 890
        pipePos_x2 = width
    
    return upPipPos_y, downPipPos_y, upPipPos_y2, downPipPos_y2, pipePos_x, pipePos_x2

def changePosCounter(screen,displayText,width,height,countPoints):
    if countPoints < 10:
        screen.blit(displayText,(width/2,height-600))
    else:
        screen.blit(displayText,((width/2)-30,height-600))

def showAllImages(screen,bird_x,bird_y,backgroundResizeImage,upPipeResizeImage,downPipeRisezeImage,upPipeResizeImage2,downPipeRisezeImage2,birdResizeImage,pipePos_x,pipePos_x2,upPipPos_y,downPipPos_y,upPipPos_y2,downPipPos_y2):
    screen.fill((0,0,0)) # Screen clean
    screen.blit(backgroundResizeImage,(0,0))
    screen.blit(upPipeResizeImage, (pipePos_x, upPipPos_y))
    screen.blit(downPipeRisezeImage, (pipePos_x, downPipPos_y))
    screen.blit(upPipeResizeImage2, (pipePos_x2, upPipPos_y2))
    screen.blit(downPipeRisezeImage2, (pipePos_x2, downPipPos_y2))
    screen.blit(birdResizeImage,(bird_x,bird_y))

def changeMoves(pipePos_x,pipePos_x2,velBird,bird_y,velocityPipeMove,gravity):
    pipePos_x -= velocityPipeMove
    pipePos_x2 -= velocityPipeMove
    velBird += gravity
    bird_y += velBird

    return pipePos_x,pipePos_x2,velBird,bird_y,velocityPipeMove,gravity
