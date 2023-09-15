import pygame
import GameFunctions as GF
import ExcelFunctions as EF

# Init Vars
registPass,registPass2,width,height,start,bird_x,bird_y,countPoints,velBird,gravity,pipePos_x,pipePos_x2,textColor,running,impulse,velocityPipeMove,upPipPos_y,upPipPos_y2,downPipPos_y,downPipPos_y2,upPipPos_y_min,upPipPos_y_max = GF.initVars()

# Pygame setup
pygame.init()
screen,clock,font,displayText = GF.pygameSetup(width,height,countPoints,textColor)

# Load Images
backgroundResizeImage, upPipeResizeImage, downPipeRisezeImage, upPipeResizeImage2, downPipeRisezeImage2, flappyBirdTextResizeImage, birdResizeImage, playButtonResizeImage = GF.loadImages(width,height)

# Load/Create Excel
sheet,workbook = EF.createExcelFile()

# Create Colluns
sheet = EF.addCollunsToExcel(sheet)

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
        #Change Movements(Bird/Pipes)
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
        start, bird_rect, up_pipe_rect, up_pipe_rect2, down_pipe_rect, down_pipe_rect2 = EF.touchPipes(bird_x,bird_y,birdResizeImage,pipePos_x,pipePos_x2,upPipPos_y,upPipPos_y2,width,height,start)

        ################################### Add Data to Excel ###################################
        row = sheet.max_row + 1
    
        centeryBird = bird_rect.centery
        centerxBird = bird_rect.centerx

        distancia_x_up = up_pipe_rect.bottomleft[0] - centerxBird
        distancia_y_up = up_pipe_rect.bottomleft[1] - centeryBird
        distancia_x_down = down_pipe_rect.topleft[0] - centerxBird
        distancia_y_down = down_pipe_rect.topleft[1] - centeryBird
        distanciaCornerUpPip = (distancia_x_up ** 2 + distancia_y_up ** 2) ** 0.5
        distanciaCornerDownPip = (distancia_x_down ** 2 + distancia_y_down ** 2) ** 0.5

        distancia_x_up2 = up_pipe_rect2.bottomleft[0] - centerxBird
        distancia_y_up2 = up_pipe_rect2.bottomleft[1] - centeryBird
        distancia_x_down2 = down_pipe_rect2.topleft[0] - centerxBird
        distancia_y_down2 = down_pipe_rect2.topleft[1] - centeryBird
        distanciaCornerUpPip2 = (distancia_x_up2 ** 2 + distancia_y_up2 ** 2) ** 0.5
        distanciaCornerDownPip2 = (distancia_x_down2 ** 2 + distancia_y_down2 ** 2) ** 0.5

        if centerxBird < up_pipe_rect.bottomleft[0]:
            sheet[f"A{row}"] = centeryBird
            sheet[f"B{row}"] = distanciaCornerUpPip
            sheet[f"C{row}"] = distanciaCornerDownPip
        
        if centerxBird < up_pipe_rect2.bottomleft[0]:
            sheet[f"A{row}"] = centeryBird
            sheet[f"D{row}"] = distanciaCornerUpPip2
            sheet[f"E{row}"] = distanciaCornerDownPip2
        ######################################## End ########################################

    pygame.display.flip() # Update Screen
    clock.tick(60) # FPS to 60

# Save and Close Excel
EF.saveAndCloseExcel(workbook)

pygame.quit()