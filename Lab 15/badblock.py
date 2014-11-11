import pygame
import my_classes
import random

class BadBlock(my_classes.Block):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame
    """
 
    def __init__(self, filename,colorkey):
           # Call the parent class (Sprite) constructor
        super().__init__(filename,colorkey) 
   
    def update(self):
            """ Find a new position for the player"""
            self.rect.y += 1
            if self.rect.y > 400:
                self.rect.y = -1
                self.rect.x = random.randrange(0,700)