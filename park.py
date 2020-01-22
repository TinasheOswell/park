#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pygame
def main():
    worldmap = Map()
    worldmap.openwindow()

class Map:
    Window = None
    #has tiles 
    #you is Ishara
    #me is me
    def openwindow(self):
        #opens the window
        self.Window = pygame.display.set_mode((1000,600))
        pygame.display.set_caption("Parking")

        #keeps it open until the x is clicked
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


    def drawtile(self):
        #draw the grid
        #initial all black squares
        pass #me
    def makevalid(self, valid_tile_list):
        ## how should this work?
            ##add tiles to a valid tile list OR
            ##change the tile attribute valid to true??
        # and here
        #makes a tile valid for car motion etc
        pass #you
    
    def makeparkingspots(self):
        #uses (x,y) coordinates
        #makes certain tiles for parking
        pass #me
    
    def freepark(self, parking_center):
        #make calculation depending on how wide and high the tiles are to
            ##determine how many tiles to the left and to the right
        #randomly picks a spot from the parking spaces and makes it the goal
        pass #you
    
    def make_path(self):
        #makes tiles valid for driving
        pass #me
    
    


# In[ ]:


class Tile:
    pass
    #attributes :
        #color, parking or not path or not you
        # draws itself me
        #location and size you
        


main()



