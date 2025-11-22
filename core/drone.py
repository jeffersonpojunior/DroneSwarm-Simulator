import pygame
import matplotlib as plot
import numpy as np

class Drone:
    def __init__(self, id, position, velocity, config):
        self.id = id
        self.position = position
        self.velocity = velocity
        self.config = config

    def getPosition(self):
        return self.position
    
    def getVelocity(self):
        return self.velocity
    
    def getID(self):
        return self.id
    
    