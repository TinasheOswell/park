
import pygame, time, os
from uagame import Window
from pygame.locals import *
import math
from random import shuffle, randint

def main():

    window = Window('PARK', 1500, 800)
    window.set_auto_update(False)
    map = Map(window)
    #pass map to car
    map.play()
    #window.close()

class Map:
    def __init__(self,window):
        self.window = window
        Tile.set_window(window)
        self.bg_color = 'black'
        self.close_clicked = False
        self.Continue = True

        self.size = (1500, 800)
        self.map = []
        self.parkingSpots = []
        self.tile_dim = (15, 8)
        Tile.set_dimen(self.tile_dim)
        self.makeTiles()
        self.makevalidroad([7, 6])
        self.create_pspots()

    def makeTiles(self):
        for col_i in range(0, self.get_size()[1]):
            row = []
            for row_i in range(0, self.get_size()[0]):
                tile = self.maketile([(row_i * self.tile_dim[0]), (col_i*self.tile_dim[1])])
                row.append(tile)
            self.map.append(row)

    def maketile(self, location):
        tile = Tile(False, False, location)
        return tile

    def makevalidroad(self, start_index):
        ## how should this work?
            ##add tiles to a valid tile list OR
            ##change the tile attribute valid to true??
        # and here
        #makes a tile valid for car motion etc
        for i in range (start_index[1], 90):
            #self.map[100-start_index[0]][6].valid_road = True
            bottom_index = [100-start_index[0],start_index[1]]
            #top_index = [start_index]
            self.path(start_index,False,True)
            start_index[1] = start_index[1]+1
            self.path(bottom_index, False, True)

        for i in range (start_index[0], 94 ):
            rightindex = [start_index[0],start_index[1]+2]
            self.path(rightindex, True, False)
            self.path([start_index[0], start_index[1]-6], True, False)
            self.path([start_index[0], start_index[1] - 15], True, False)
            self.path([start_index[0], start_index[1] - 24], True, False)
            self.path([start_index[0], start_index[1] - 33], True, False)
            start_index[0] = start_index[0] + 1

        umiddle_index = [40, 6]
        bmiddle_index = [60, 6]
        for i in range(6, 55):
            self.path(umiddle_index, False, True)
            umiddle_index[1] = umiddle_index[1] + 1
            self.path(bmiddle_index, False, True)
            bmiddle_index[1] = bmiddle_index[1] + 1

        rightindex = [6, 6]
        for i in range(6, 41):
            self.path(rightindex, True, False)
            rightindex[0] = rightindex[0] + 1

        rightindex = [60, 6]
        for i in range(6, 41):
            self.path(rightindex, True, False)
            rightindex[0] = rightindex[0] + 1

    def path (self, tile_index, vertical, horizontal):
        #road_size = int ((12000 / (self.num_of_grids)))*2
        if vertical:
            for i in range (0, 3):
                self.map[tile_index[0]][tile_index[1]-i].valid_road = True
                self.map[tile_index[0]][tile_index[1]+i].valid_road = True
        else:
            for i in range (0, 4):
                self.map[tile_index[0] + (i)][tile_index[1]].valid_road = True
                self.map[tile_index[0] - (i)][tile_index[1]].valid_road = True
                self.map[tile_index[0]-(i+1)][tile_index[1]].valid_road = True
                self.map[tile_index[0]+(i+1)][tile_index[1]].valid_road = True

    def play(self):

        while not self.close_clicked:  # until user clicks close box
            # play frame
            self.handle_event()
            self.draw()
            if self.Continue:
                self.update()
                self.decide_continue()

    def handle_event(self):
        # Handle each user event by changing the game state
        # appropriately.
        # - self is the Game whose events will be handled

        event = pygame.event.poll()
        if event.type == QUIT:
            self.close_clicked = True
            #self.window.close()


        #elif event is left, right, up, down (controls for car)
            #handle up
            #handle down
            #handle left
            #handle right
        #eg:
        #elif event.type == MOUSEBUTTONUP and self.continue_game:
            #self.handle_mouse_up_event(event)
    def handle_up(self,event):
        pass
    def handle_down(self,event):
        pass
    def handle_left(self,event):
        pass
    def handle_right(self,event):
        pass

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw
        # clears and redraws
        ## switch to draw just a section???
        self.window.clear()
        for row in self.map:
            for tile in row:
                tile.draw()
        #self.draw_score()
        self.window.update()

    def update(self):
        # Update the game objects.
        # what do we update???
        #if self.Continue:
        pass

    def decide_continue(self):
        # Check and remember if the game should continue
        # when to finish the run
        #
        #if run_should_finish:
            #self.Continue= False
        pass

    def create_pspots(self):
        j=12
        for i in range(9, 54, 2):
            first = self.map[j][i]
            sec = self.map[j][i+1]
            third = self.map[j+1][i]
            last = self.map[j+1][i+1]
            self.make_pspot([first, sec, third, last])
        j=17
        for i in range(9, 54, 2):
            first = self.map[j][i]
            sec = self.map[j][i+1]
            third = self.map[j+1][i]
            last = self.map[j+1][i+1]
            self.make_pspot([first, sec, third, last])
        
        j=22
        for i in range(9, 54, 2):
            first = self.map[j][i]
            sec = self.map[j][i+1]
            third = self.map[j+1][i]
            last = self.map[j+1][i+1]
            self.make_pspot([first, sec, third, last])
        j=27
        for i in range(9, 54, 2):
            first = self.map[j][i]
            sec = self.map[j][i+1]
            third = self.map[j+1][i]
            last = self.map[j+1][i+1]
            self.make_pspot([first, sec, third, last])
        j = 35
        for i in range(9, 54, 2):
            first = self.map[j][i]
            sec = self.map[j-1][i]
            third = self.map[j-2][i]
            last = self.map[j-3][i]
            five = self.map[j-4][i]
            self.make_pspot([first, sec, third, last, five])
        
        j=12 + 53
        for i in range(9, 54, 2):
            first = self.map[j][i]
            sec = self.map[j][i+1]
            third = self.map[j+1][i]
            last = self.map[j+1][i+1]
            self.make_pspot([first, sec, third, last])
        j=17+ 53
        for i in range(9, 54, 2):
            first = self.map[j][i]
            sec = self.map[j][i+1]
            third = self.map[j+1][i]
            last = self.map[j+1][i+1]
            self.make_pspot([first, sec, third, last])
        
        j=22+ 53
        for i in range(9, 54, 2):
            first = self.map[j][i]
            sec = self.map[j][i+1]
            third = self.map[j+1][i]
            last = self.map[j+1][i+1]
            self.make_pspot([first, sec, third, last])
        j=27+ 53
        for i in range(9, 54, 2):
            first = self.map[j][i]
            sec = self.map[j][i+1]
            third = self.map[j+1][i]
            last = self.map[j+1][i+1]
            self.make_pspot([first, sec, third, last])
        j = 35+ 53
        for i in range(9, 54, 2):
            first = self.map[j][i]
            sec = self.map[j-1][i]
            third = self.map[j-2][i]
            last = self.map[j-3][i]
            five = self.map[j-4][i]
            self.make_pspot([first, sec, third, last, five])

    def make_pspot(self, tiles):
        parking_s = ParkingSpot(tiles)
        self.parkingSpots.append(parking_s)
        
    def get_size(self):
        return self.size

# +
class Tile:
    window = None
    dimen = None

    blue_col = pygame.Color(46, 80, 143)
    white_col = pygame.Color(255, 255, 255)
    boarder_width = 1



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
        self.color = pygame.Color("green")
        self.boarder = Tile.boarder_width
        
    def changecol(self, val):
        self.color = val
        
    def validpark(self, val):
        self.valid_park = val
        
#     def ctest(self):
#         self.test = True
        
    def getRect(self):
        return self.rectangle
    
    def updatec(self):
        if self.valid_park:
            self.boarder = 0
        elif self.valid_road:
            self.color = Tile.white_col
#         elif self.test:
#             self.color = pygame.Color(255, 0, 0)
        else:
            self.color = Tile.blue_col
        
    def draw(self):
        self.updatec()
        pygame.draw.rect(Tile.window.get_surface(), self.color, self.rectangle, self.boarder)


# -

class ParkingSpot:
    def __init__(self, tiles, rects=False, location = []):
        color = pygame.Color(randint(0,255), randint(0,255), randint(0,255))
        ls=[]
        for tile in tiles:
            tile.validpark(True)
            tile.changecol(color)
            ls.append(tile.getRect())
        
        rec = ls.pop(0)
        self.rect = rec.unionall(ls)


main()


