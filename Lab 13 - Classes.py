import pygame
import random
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

# Classes
class Rectangle():
    # --- Class Attributes ---
    x = 0 
    y = 0 
    height = 0
    width = 0
    change_x = 0
    change_y = 0
    color = WHITE
    # --- Class Methods ---
    def __init__(self,x,y,height,width,color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color
    def draw(self):
        pygame.draw.rect(screen,self.color,[self.x,self.y,self.height,self.width],0)
    def move(self,change_x,change_y):
        self.change_x = change_x
        self.change_y = change_y
        self.x += self.change_x
        self.y += self.change_y
class Ellipse(Rectangle):
    def draw(self):
        pygame.draw.ellipse(screen,self.color,[self.x,self.y,self.height,self.width],0)
# Pygame StartUp
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Variables
done = False
myList = []
loop_count = 1000
for i in range(loop_count):
    myObject = Rectangle(random.randrange(0,700),random.randrange(0,500),random.randrange(20,70),random.randrange(20,70),[random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)])
    myList.append(myObject)
for i in range(loop_count):
    myObject = Ellipse(random.randrange(0,700),random.randrange(0,500),random.randrange(20,70),random.randrange(20,70),[random.randrange(0,255),random.randrange(0,255),random.randrange(0,255)])
    myList.append(myObject)

 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
 
    # --- Game logic should go here
        
    # --- Drawing code should go here
    screen.fill(BLACK)
    for shape in myList:
        shape.draw()
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()