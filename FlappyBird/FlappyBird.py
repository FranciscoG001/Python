import pygame
import GameFunctions as GF

# Init Vars
registPass,registPass2,width,height,start,bird_x,bird_y,countPoints,velBird,gravity,pipePos_x,pipePos_x2,textColor,running,impulse,velocityPipeMove,upPipPos_y,upPipPos_y2,downPipPos_y,downPipPos_y2,upPipPos_y_min,upPipPos_y_max = GF.initVars()

# Pygame setup
pygame.init()
screen,clock,font,displayText = GF.pygameSetup(width,height,countPoints,textColor)

# Load Images
backgroundResizeImage, upPipeResizeImage, downPipeRisezeImage, upPipeResizeImage2, downPipeRisezeImage2, flappyBirdTextResizeImage, birdResizeImage, playButtonResizeImage = GF.loadImages(width,height)

# Pygame Loop
while running:

    # Actions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start,bird_x,bird_y,velBird,gravity,pipePos_x,pipePos_x2,countPoints,displayText = GF.startGameParameters(width,height,font,textColor)
            if event.key == pygame.K_SPACE:
                velBird = impulse
            if event.key == pygame.K_ESCAPE:
                start = False
    
    # Start Page Images
    GF.startPageImages(screen,backgroundResizeImage,flappyBirdTextResizeImage,birdResizeImage,playButtonResizeImage,width,height)

    if start:
        # Change Movements(Bird/Pipes)
        pipePos_x,pipePos_x2,velBird,bird_y,velocityPipeMove,gravity = GF.changeMoves(pipePos_x,pipePos_x2,velBird,bird_y,velocityPipeMove,gravity)

        # Show all imagens
        GF.showAllImages(screen,bird_x,bird_y,backgroundResizeImage,upPipeResizeImage,downPipeRisezeImage,upPipeResizeImage2,downPipeRisezeImage2,birdResizeImage,pipePos_x,pipePos_x2,upPipPos_y,downPipPos_y,upPipPos_y2,downPipPos_y2)

        # Change position of point counter
        GF.changePosCounter(screen,displayText,width,height,countPoints)
        
        # Reset Pip
        upPipPos_y, downPipPos_y, upPipPos_y2, downPipPos_y2, pipePos_x, pipePos_x2 = GF.resetPipes(pipePos_x,pipePos_x2,upPipeResizeImage,upPipeResizeImage2,upPipPos_y_max,upPipPos_y_min,width,upPipPos_y,upPipPos_y2,downPipPos_y,downPipPos_y2)

        # Ground or Sky Touch - Lost
        start = GF.groundOrSkyTouch(bird_y,start)

        # Count points
        countPoints, displayText, registPass, registPass2 = GF.countPoints(bird_x, pipePos_x, pipePos_x2, upPipeResizeImage, upPipeResizeImage2, registPass, registPass2, countPoints, displayText, font, textColor)

        # Touch Pipes
        start = GF.touchPipes(bird_x,bird_y,birdResizeImage,pipePos_x,pipePos_x2,upPipPos_y,upPipPos_y2,width,height,start)
        
    pygame.display.flip() # Update Screen
    clock.tick(60) # FPS to 60

pygame.quit()