import pygame
import random

# Init setup vars
width = 640
height = 720

running = True
start = False

countPoints = 0
textColor = (255, 255, 255)

# Init possition
bird_x = (width/2)-20
bird_y = height / 2

# Movement
velBird = 0  
gravity = 0.5
impulse = -9
velocityPipeMove = 5
pipePos_x = width
pipePos_x2 = width * 2

# Start coords
upPipPos_y = -350
upPipPos_y2 = -250
downPipPos_y = 500
downPipPos_y2 = 600

# To random pipes
upPipPos_y_min = -250
upPipPos_y_max = -550

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

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 100)
displayText = font.render(str(countPoints), True, textColor)

# Convert to avoid the black pixeis of image
birdResizeImage = birdResizeImage.convert_alpha()
upPipeResizeImage = upPipeResizeImage.convert_alpha()
downPipeRisezeImage = downPipeRisezeImage.convert_alpha()
upPipeResizeImage2 = upPipeResizeImage2.convert_alpha()
downPipeRisezeImage2 = downPipeRisezeImage2.convert_alpha()

# Pygame Loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False # QUIT
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start = True # Start game
                bird_x = (width/2)-20
                bird_y = height / 2
                velBird = 0  
                gravity = 0.5
                pipePos_x = width
                pipePos_x2 = width + 400
                countPoints = 0
                displayText = font.render(str(countPoints), True, textColor)
            if event.key == pygame.K_SPACE:
                velBird = impulse # Bird Jump
            if event.key == pygame.K_ESCAPE:
                start = False # Stop Game
    
    screen.blit(backgroundResizeImage,(0,0))
    screen.blit(flappyBirdTextResizeImage,(0,0))
    screen.blit(birdResizeImage,((width/2)-20,height/2))
    screen.blit(playButtonResizeImage,((width/2)-60,(height/2)-130))

    if start:
        
        # Pips Move Velocity
        pipePos_x -= velocityPipeMove
        pipePos_x2 -= velocityPipeMove

        # Bird Move
        velBird += gravity
        bird_y += velBird

        # Screen clean
        screen.fill((0,0,0))
        
        # Show all imagens
        screen.blit(backgroundResizeImage,(0,0))
        screen.blit(upPipeResizeImage, (pipePos_x, upPipPos_y))
        screen.blit(downPipeRisezeImage, (pipePos_x, downPipPos_y))
        screen.blit(upPipeResizeImage2, (pipePos_x2, upPipPos_y2))
        screen.blit(downPipeRisezeImage2, (pipePos_x2, downPipPos_y2))

        if countPoints < 10:
            screen.blit(displayText,(width/2,height-600))
        else:
            screen.blit(displayText,((width/2)-30,height-600))
        screen.blit(birdResizeImage,(bird_x,bird_y))
        
        # Reset Pip
        if pipePos_x + upPipeResizeImage.get_width() < -50:
            upPipPos_y = random.randint(upPipPos_y_max,upPipPos_y_min) # New position
            downPipPos_y = upPipPos_y + 850
            pipePos_x = width
        # Reset Pip2
        if pipePos_x2 + upPipeResizeImage2.get_width() < -50:
            upPipPos_y2 = random.randint(upPipPos_y_max,upPipPos_y_min) # New position
            downPipPos_y2 = upPipPos_y2 + 850
            pipePos_x2 = width

        # Ground Touch
        if bird_y > 600:
            start = False

        # Count Pip
        if bird_x > pipePos_x + upPipeResizeImage.get_width() and not passagem_registrada:
            countPoints += 1
            displayText = font.render(str(countPoints), True, textColor)
            passagem_registrada = True
        elif bird_x <= pipePos_x + upPipeResizeImage.get_width():
            passagem_registrada = False
        # Count Pip2
        if bird_x > pipePos_x2 + upPipeResizeImage2.get_width() and not passagem_registrada2:
            countPoints += 1
            displayText = font.render(str(countPoints), True, textColor)
            passagem_registrada2 = True
        elif bird_x <= pipePos_x2 + upPipeResizeImage2.get_width():
            passagem_registrada2 = False

        # Touch Pipes

        

        
        

    pygame.display.flip() # Update Screen
    clock.tick(60) # FPS to 60

pygame.quit()

