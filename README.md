# park
reinforcement learning parking system

Class Car:
	Drive: increases the velocity of the car by 1 unit (if the car is in forward motion):
	Reverse: decreases the velocity of the car by 1 unit (if the car is in backward motion):
	Right: turns the car wheels by 1 degree(unit) to the right:
	Left: turns the car wheels by 1 degree to the left:
Stop: stops the movement of the car in any direction:
	
	Optional fuel???

	Object detection: front, back, left and right, tl, tr, br, bl

	Car position is given by the centre of the car
	If car moves into outside bounds it crashes and resets
	If it moves into objects it also crashes and resets

Class map:

Made up of small grids which are each 1cm * 1cm 
The entire maps is 12 000 grids by 34 200 grids.
Each parking spot is blah blah * blah blah
The road size is 2 * parking spot size.
