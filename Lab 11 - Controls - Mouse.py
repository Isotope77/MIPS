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
# Hides Mouse Cursor
pygame.mouse.set_visible(False)

# ----------------MAIN PROGRAM LOOP---------------------------------
while not done:
    # Main Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # Game Logic
    pos = pygame.mouse.get_pos()
    x_coord = pos[0]
    y_coord = pos[1]
    # Drawing Code
    screen.fill(BLACK)
    drawsquare(x_coord,y_coord)
    # Update Screen with Drawing
    pygame.display.flip()
    # Limit 60 fps
    clock.tick(60)
#Close the window and quit
pygame.quit()
