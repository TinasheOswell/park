#!/usr/bin/env python
# coding: utf-8
# %%

# %%
import os
import pygame

class Car:
    def __init__(self, window):
        self.window = window
        self.colour = None
        self.length = None
        self.width = None
        self.location = (0,0)
        self.velocity = [0,0]
        self.angle = 0.0
    
    def drive(self):
        if self.velocity[0] >= 0 and self.velocity[1] >=0:
            self.velocity[0] += 1
            self.velocity[1] += 1
    
    def reverse(self):
        if self.velocity[0] <= 0 and self.velocity[1] <=0:
            self.velocity[0] += 1
            self.velocity[1] += 1   
    
    def stop(self):
        self.velocity = [0,0]
        
    def move(self):
        pos = self.location + self.velocity

    def load_car(self):
        dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(dir, "car.png")
        car_image = pygame.image.load(image_path)
        car_image = pygame.transform.scale(car_image, (50, 25))
        return car_image

    
        

