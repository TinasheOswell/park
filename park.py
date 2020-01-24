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
    
    def __init__(self):
        self.map = []
        self.makeTiles()
    
    def openwindow(self):
        #opens the window
        self.Window = pygame.display.set_mode((1500,800))
        Tile.set_window(self.Window)
        pygame.display.set_caption("Parking")

        self.drawtile() #draws the initial tile display need to move
        
        #keeps it open until the x is clicked
        running = True
        while running:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


    def maketile(self, location):
        tile = Tile(False, False, location)
        return tile
    
    def makeTiles(self):
        for row_i in range(0, 65):
            col = []
            for col_i in range(0, 53):
                tile = self.maketile([(row_i * 23), (col_i*15)])
                col.append(tile)
            self.map.append(col)

    def drawtile(self):
        #draw the grid
        #initial all black squares
        count = 0
        for row in self.map:
            for tile in row:
                count = count + 1
                tile.draw(count)
        #me

    def makevalidroad(self, valid_tile_list):
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
        #### not neccesary ### this function is lije makevalidroad ###
        pass #me
    
    


# In[ ]:


class Tile:
    
    window = None
    back_col = pygame.Color(46, 80, 143)
    boarder_width = 1
    
    @classmethod
    def set_window(cls, window):
        cls.window = window

    def __init__(self, valid_road, valid_park, location):
        self.valid_road = valid_road
        self.valid_park = valid_park
        self.location = location
        self.rectangle = pygame.Rect(location[0], location[1], 23,15)
        
    def draw(self):
        #draw itself
        #me
        pygame.draw.rect(Tile.window, Tile.back_col, self.rectangle, Tile.boarder_width)


    #attributes :
        #(valid road, valid park, none)
        #color, parking or not path or not you
        # draws itself me
        #location and size you
        


main()



