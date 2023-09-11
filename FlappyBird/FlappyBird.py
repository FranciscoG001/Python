import pygame

# Init setup vars
width = 640
height = 720

running = True
start = False

velocityPipeMove = 5
pipePos_x = width
textColor = (255, 255, 255)

backgroundImage = pygame.image.load("Images/background.jpg")
upPipeImage = pygame.image.load("Images/upPipe.png")
downPipeImage = pygame.image.load("Images/downPipe.png")
flappyBirdTextImage = pygame.image.load("Images/flappyBirdText.png")
birdImage = pygame.image.load("Images/bird.png")
playButtonImage = pygame.image.load("Images/playbtn.png")

backgroundResizeImage = pygame.transform.scale(backgroundImage, (width, height))
upPipeResizeImage = pygame.transform.scale(upPipeImage, (width/7, height))
downPipeRisezeImage = pygame.transform.scale(downPipeImage, (width/7, height))
flappyBirdTextResizeImage = pygame.transform.scale(flappyBirdTextImage, (width, 200))
birdResizeImage = pygame.transform.scale(birdImage, (75, 75))
playButtonResizeImage = pygame.transform.scale(playButtonImage, (150, 75))

# Posição inicial do pássaro
bird_x = (width/2)-20
bird_y = height / 2

velBird = 0  
gravity = 0.5
impulse = -9
countPoints = 0

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
                countPoints = 0
                displayText = font.render(str(countPoints), True, textColor)
            if event.key == pygame.K_SPACE:
                velBird = impulse # Bird Jump
            if event.key == pygame.K_ESCAPE:
                start = False # Stop Game
    
    screen.blit(backgroundResizeImage,(0,0))
    screen.blit(flappyBirdTextResizeImage,(0,0))
    screen.blit(birdResizeImage,((width/2)-20,height/2))
    screen.blit(playButtonResizeImage,((width/2)-55,(height/2)-130))

    if start:
        pipePos_x -= velocityPipeMove

        velBird += gravity
        bird_y += velBird

        screen.fill((0,0,0))

        screen.blit(backgroundResizeImage,(0,0))
        screen.blit(upPipeResizeImage, (pipePos_x, -350))
        screen.blit(downPipeRisezeImage, (pipePos_x, 500))
        screen.blit(displayText,(width/2,height-600))
        screen.blit(birdResizeImage,(bird_x,bird_y))
        
        if pipePos_x + upPipeResizeImage.get_width() < 0:
            pipePos_x = width

        if bird_x > pipePos_x + upPipeResizeImage.get_width() and not passagem_registrada:
            countPoints += 1
            displayText = font.render(str(countPoints), True, textColor)
            passagem_registrada = True
        elif bird_x <= pipePos_x + upPipeResizeImage.get_width():
            passagem_registrada = False
        
        # Verifique se o pássaro colidiu com os tubos (tanto tubo de cima quanto tubo de baixo)
        if (
            # Colisão com o tubo de cima
            (bird_x + birdResizeImage.get_width() > pipePos_x and bird_x < pipePos_x + upPipeResizeImage.get_width())
            and
            (bird_y < -350 or bird_y + birdResizeImage.get_height() > 600 )
        ) or (
            # Colisão com o tubo de baixo
            (bird_x + birdResizeImage.get_width() > pipePos_x and bird_x < pipePos_x + downPipeRisezeImage.get_width())
            and
            (bird_y < -350 + 700 or bird_y + birdResizeImage.get_height() > 500)
        ):
            start = False  # Encerre o jogo se houver uma colisão

    pygame.display.flip() # Update Screen
    clock.tick(60) # FPS to 60

pygame.quit()

