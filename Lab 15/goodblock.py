import pygame
import my_classes
import random

class Goodblock(my_classes.Block):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame
    """
 
    def __init__(self, filename,colorkey):
           # Call the parent class (Sprite) constructor
        super().__init__(filename,colorkey) 
   
    def update(self):
            """ Find a new position for the player"""
            self.rect.x += random.randint(-3,3)
            self.rect.y += random.randint(-3,3)