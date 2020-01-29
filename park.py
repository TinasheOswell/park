#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pygame
def main():
    worldmap = Map()
    #worldmap.openwindow()

class Map:
    #Window = None
    #why?? Window = None
    #has tiles 
    #you is Ishara
    #me is me
    def __init__(self):
        self.map = []
        self.size = (1500, 800)
        self.tile_dim = (15, 8)
        Tile.set_dimen(self.tile_dim)
        self.makeTiles()
        self.makevalidroad([6,6])
        self.openwindow()
        
    def openwindow(self):
        #opens the window
        self.Window = pygame.display.set_mode(self.get_size())
        Tile.set_window(self.Window)
        pygame.display.set_caption("Parking")

        self.drawtile() #draws the initial tile display need to move
        
        #keeps it open until the x is clicked
        running = True
        while running:
            pygame.display.flip() #to be deleted and moved from this area once appropriate methods are made
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
    
    #creates a new instance of Tile
    #location is the location in pixels not row/col number
    def maketile(self, location):
        tile = Tile(False, False, location)
        return tile
    
    #calls the maketile method and creates a grid of tiles to be used as the map
    def makeTiles(self):
        for col_i in range(0, self.get_size()[1]):
            row = []
            for row_i in range(0, self.get_size()[0]):
                tile = self.maketile([(row_i * self.tile_dim[0]), (col_i*self.tile_dim[1])])
                row.append(tile)
            self.map.append(row)

    #displays the tile objects of the map on the pygame display window
    def drawtile(self):
        #draw the grid
        #initial all black squares
        count = 0
        for row in self.map:
            for tile in row:
                count = count + 1
                tile.draw(count)
        #me

    def makevalidroad(self, start_index):
        ## how should this work?
            ##add tiles to a valid tile list OR
            ##change the tile attribute valid to true??
        # and here
        #makes a tile valid for car motion etc
        for i in range (start_index[0], 76):
            self.path(start_index,False,True)
            start_index[1] = start_index[1]+1

        for i in range (start_index[1], 50):
            self.path

    def path (self, tile_index, vertical, horizontal):
        if vertical:
            for i in range (0, 2):
                self.map[tile_index[0]][tile_index[1]-i].valid_road = True
                self.map[tile_index[0]][tile_index[1]+i].valid_road = True
        else:
            for i in range (0, 2):
                self.map[tile_index[0]-i][tile_index[1]].valid_road = True
                self.map[tile_index[0]+i][tile_index[1]].valid_road = True

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
    
    def get_size(self):
        return self.size
    
    
# In[ ]:


class Tile:
    
    window = None
    blue_col = pygame.Color(46, 80, 143)
    white_col = pygame.Color(255,255,255)
    boarder_width = 1
    dimen = None
    
    @classmethod
    def set_window(cls, window):
        cls.window = window
    
    @classmethod
    def set_dimen(cls, dim):
        cls.dimen = dim
    
    def __init__(self, valid_road, valid_park, location):
        self.valid_road = valid_road
        self.valid_park = valid_park
        self.location = location
        self.rectangle = pygame.Rect(location[0], location[1], Tile.dimen[0], Tile.dimen[1])
        
    def draw(self, count):
        if self.valid_road:
            pygame.draw.rect(Tile.window, Tile.white_col, self.rectangle, Tile.boarder_width)
        else:
            pygame.draw.rect(Tile.window, Tile.blue_col, self.rectangle, Tile.boarder_width)
        #draw itself
        #me
        #print("called" + str(count))
        


    #attributes :
        #(valid road, valid park, none)
        #color, parking or not path or not you
        # draws itself me
        #location and size you
        


main()
pygame.quit()


