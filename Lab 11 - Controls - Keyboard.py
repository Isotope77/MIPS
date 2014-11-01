import pygame

# Colors
BLACK = (  0,  0,  0)
WHITE = (255,255,255)  

pygame.init()

# Set Width and Height of Screen [Width, Height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Controls Tests")

# ----------------FUNCTIONS------------------
def drawsquare(x_coord,y_coord):
    """Draws a White Square"""
    pygame.draw.rect(screen, WHITE, [x_coord,y_coord,50,50],0)
    
# Loop until the user uses the close button
done = False 
# Manages Screen Update
clock = pygame.time.Clock()

# Speed & Coord
x_speed = 0
y_speed = 0
x_coord = 10
y_coord = 10

# ----------------MAIN PROGRAM LOOP---------------------------------
while not done:
    # Main Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0
    # Game Logic
    x_coord += x_speed
    y_coord += y_speed
    if y_coord <= 0 or y_coord >= 450:
        y_coord = y_coord * -1
    if x_coord <= 0 or x_coord >= 650:
        x_coord = x_coord * -1
    # Drawing Code
    screen.fill(BLACK)
    drawsquare(x_coord,y_coord)
    # Update Screen with Drawing
    pygame.display.flip()
    # Limit 60 fps
    clock.tick(60)
#Close the window and quit
pygame.quit()
