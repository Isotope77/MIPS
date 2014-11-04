#Chapter 12 Lab - Images and Sound

import pygame

# Colors
WHITE = (255, 255, 255)
GRAY  = ( 23,  23,  23)
BLACK = (  0,   0,   0)

# Pygame/Window Set Up
pygame.init()
size = [800,600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Images and Sound Test")
clock = pygame.time.Clock()

# -----------Functions------------------
def starship_speed():
    starship_position[0] += speed[0]
    starship_position[1] += speed[1]
    if starship_position[0] <= 0 or starship_position[0] >= size[0]-50:
        starship_position[0] = starship_position[0] * -1
    if starship_position[1] <= 0 or starship_position[1] >= size[1]-75:
        starship_position[1] = starship_position[1] * -1      
        
# Set Variables
background_position = [0,0]
starship_position = [0,0]
speed = [0,0]

# Load Sounds
space_sound = pygame.mixer.Sound(r"C:\Users\gneville\Documents\GitHub\MIPS\Lab 12\laser.ogg")

# Load Pictures
background_image = pygame.image.load(r"C:\Users\gneville\Documents\GitHub\MIPS\Lab 12\background.jpg").convert()
starship_image = pygame.image.load(r"C:\Users\gneville\Documents\GitHub\MIPS\Lab 12\starship.png").convert()
starship_image.set_colorkey(WHITE)

# ----------------MAIN PROGRAM LOOP---------------------------------
done = False
while not done:
    # Main Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speed[0] = -3
            if event.key == pygame.K_RIGHT:
                speed[0] = 3
            if event.key == pygame.K_UP:
                speed[1] = -3
            if event.key == pygame.K_DOWN:
                speed[1] = 3
            if event.key == pygame.K_SPACE:
                space_sound.play()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                speed[0] = 0
            if event.key == pygame.K_RIGHT:
                speed[0] = 0
            if event.key == pygame.K_UP:
                speed[1] = 0
            if event.key == pygame.K_DOWN:
                speed[1] = 0
    # Game Logic
    starship_speed()
    
    # Drawing Code
    screen.fill(BLACK)
    screen.blit(background_image, background_position)
    screen.blit(starship_image, starship_position)
    # Update Screen with Drawing & limit 60 fps
    pygame.display.flip()
    clock.tick(60)
#Close the window and quit
pygame.quit()

