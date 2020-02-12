#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Car:
    def __init__(self):
        self.colour = None
        self.length = None
        self.width = None
        self.location = [0,0]
        self.velocity = [0,0]
    
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
              
    
        

